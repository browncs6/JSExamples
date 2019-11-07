from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/table')
def table():
    table = [{'name' : 'Tux', 'profession' : 'penguin'},
             {'name' : 'Sealion', 'profession' : 'sealion'}]
    return jsonify(table)

app.run(debug=True)
