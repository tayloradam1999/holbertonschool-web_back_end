#!/usr/bin/env python3
"""
Creates Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    First get endpoint
    """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    Expects two form data fields: "email" and "password".

    If the user does not exist, registers it and responds.

    If user already exists, catch exception and return JSON payload and
        returns 400
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({'email': email, 'message:': 'user created'})
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
