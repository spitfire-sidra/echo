# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask import json
from flask import jsonify
from flask import request
from flask import render_template

from echo import config


app = Flask(__name__)
app.debug = config.DEBUG
app.secret_key = config.FLASK_SESSION_SECRET_KEY
app.root_path = os.path.abspath(os.path.dirname(__file__))

json_filepath = os.path.join(app.root_path, 'echo.json')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        json_content = request.form['json_content']
        if not json_content:
            json_content = '{}'

        with open(json_filepath, 'wb') as f:
            f.write(json_content.encode('utf-8'))

    with open(json_filepath, 'rb') as f:
        json_content = f.read()

    return render_template('index.html', json_content=json_content.decode('utf-8'))


@app.route('/api')
@app.route('/api/')
@app.route('/api/<any>')
def echo(any=None):

    with open(json_filepath, 'rb') as f:
        try:
            return jsonify(**json.load(f))
        except ValueError:
            return 'please check the echo content'
