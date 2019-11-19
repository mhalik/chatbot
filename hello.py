# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:06:20 2017

@author: Max
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    