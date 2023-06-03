""" Se importan los módulos necesarios de flask """
from flask import Flask, request, jsonify, redirect, url_for, render_template
import requests
import json

app = Flask(__name__)
results = None

""" Se define la ruta principal en la raíz del proyecto """
@app.route('/', methods=['GET', 'POST'])
def index():
    # Variable global que almacenará los resultados de la FFT
    global results 

    # En caso de que se haga una petición POST (el envío de los datos para la FFT)
    if request.method == 'POST': 

        # Se solicita el formulario con los números al HTML
        numbers = request.form['numbers'] 
        numbers_copy = numbers

        numbers = numbers.replace(',', '')
        

        # En caso de que no hayan números renderiza la plantilla html que muestra error
        if not numbers: 
            return render_template('index.html', error="Error: El campo de números no puede estar vacío")

        if not numbers.isdigit():
            return render_template('index.html', error="Error: El campo de números no puede contener otros carácteres")
        
        numbers = numbers_copy

        # Separa los números que se ingresaron mediante la coma
        numbers_list = [int(num.strip()) for num in numbers.split(',')] 

        # Solicita el lenguaje del selector en el HTML
        lenguaje = request.form['lenguaje'] 

        # En caso de ser Python o C redirige al enlace correspondiente
        if lenguaje == 'python': 
            url = 'http://100.26.165.241:5000/calcular-fft-python'
        elif lenguaje == 'c':
            url = 'http://100.26.165.241:5000/calcular-fft-c'

        # Crea el diccionario con la estructura requerida
        data = {'data': numbers_list}

        # Convierte el diccionario a JSON
        json_data = json.dumps(data)

        # Envía los datos JSON a través de una solicitud POST a la url especificada en el lenguaje
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)

        # Obtener los resultados de la respuesta JSON
        results = response.json()

        # Emparejar los valores de real e imaginary
        pairs = zip(results['real'], results['imaginary'])

        # Pasar los pares de valores a la plantilla HTML y la renderiza en modo procesado
        return render_template('index.html', numbers=numbers_list, pairs=pairs)

    # Renderiza la plantilla HTML en modo normal
    return render_template('index.html', estado=True)

""" Guarda el JSON obtenido en esta ruta para ser llamado mediante el JavaScript """
@app.route('/data.json', methods=['GET'])
def get_data():
    
    # Si hay datos los serializa mediante jsonify
    if results:
        return jsonify(results)
    # Si no hay datos, retorna el JSON vacío
    else:
        return jsonify({})

def not_found(error):
    # Al no encontrar la pagina se redirige al index
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8083)
