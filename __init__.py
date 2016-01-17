from flask import Flask
from flask import jsonify
from flask import request

import services
import views
import data

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
