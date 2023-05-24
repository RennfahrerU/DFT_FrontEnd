"""Modulo de flask"""
from flask import Flask, request, jsonify, redirect, url_for, render_template
from config import config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


def not_found(error):
    # al no encontrar la pagina lo enviamos a index
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, not_found)
    app.run()
