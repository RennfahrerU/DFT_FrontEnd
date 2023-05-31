"""Modulo de flask"""
from flask import Flask, request, jsonify, redirect, url_for, render_template
import requests
import json

app = Flask(__name__)
results = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global results

    if request.method == 'POST':

        numbers = request.form['numbers']

        if not numbers:
            return render_template('index.html', error="Error: El campo 'numbers' no puede estar vacío")

        numbers_list = [int(num.strip()) for num in numbers.split(',')]

        lenguaje = request.form['lenguaje']

        if lenguaje == 'python':
            url = 'http://100.26.165.241:5000/calcular-fft-python'
        elif lenguaje == 'c':
            url = 'http://100.26.165.241:5000/calcular-fft-c'
        print(lenguaje)

        # Crear el diccionario con la estructura requerida
        data = {'data': numbers_list}

        # Convertir el diccionario a JSON
        json_data = json.dumps(data)

        # Enviar los datos JSON a través de una solicitud POST
        #url = 'http://100.26.165.241:5000/calcular-fft-python'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)

        # Obtener los resultados de la respuesta JSON
        results = response.json()
        print(results)

        # Emparejar los valores de real e imaginary
        pairs = zip(results['real'], results['imaginary'])

        # Pasar los pares de valores a la plantilla HTML
        return render_template('index.html', numbers=numbers_list, pairs=pairs)

    return render_template('index.html')

    
@app.route('/data.json', methods=['GET'])
def get_data():
    if results:
        return jsonify(results)
    else:
        return jsonify({})

def not_found(error):
    # al no encontrar la pagina lo enviamos a index
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
