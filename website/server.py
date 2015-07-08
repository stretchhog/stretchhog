import os
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, send_file, make_response, jsonify

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'server.db')
db = SQLAlchemy(app)

auth = HTTPBasicAuth()
api = Api(app)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/comics")
def paintings():
	return make_response(jsonify({'1': "number 1", '2': 'number 2'}))


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)


@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	return response

