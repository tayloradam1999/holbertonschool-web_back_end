#!/usr/bin/env python3
"""
Basic flask app.

Create a single "/" route and an <index.html> template that
outputs "Welcome to Holberton" as page title (<title>)
and "Hello world" as header (<h1>).
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('0-index.html')
