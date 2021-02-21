# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:55:30 2020

@author: msharma
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about_app():
    return 'Options v0.1'