"""Modulo de flask"""
from flask import request
from flask import Flask, request, jsonify
from fft.dft import dft

app = Flask(__name__)


@app.route('/')
def index():
    return "hola mundo"


@app.route('/calcular-fft/<lista>', methods=['GET'])
def calcular_fft(lista):
    # Separa la lista en números individuales
    lista_numeros = lista.split(',')
    # Convierte los números a enteros
    lista_numeros = [int(numero) for numero in lista_numeros]

    # Llama a la función de la FFT y obtén el resultado
    resultado_fft = calcular_fft(lista_numeros)

    # Crea un nuevo JSON con el resultado
    response = {
        'resultado': resultado_fft
    }

    return jsonify(response)  # Devuelve el resultado como JSON al frontend


if __name__ == '__main__':
    app.run(debug=True)
