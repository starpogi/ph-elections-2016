from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import render_template
from flask import abort

import services
import views
import data

base_app = Blueprint('base_app', __name__)

@base_app.route("/")
def index():
    return "Hello World"
