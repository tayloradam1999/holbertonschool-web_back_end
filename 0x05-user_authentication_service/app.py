#!/usr/bin/env python3
"""
Creates Flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    First get endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
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
    except ValueError as e:
        return jsonify({'message': 'email already registered'}), 400
    

@app.route("/sessions", methods=["POST"])
def sessions():
    """
    Expects two form data fields: "email" and "password".
    
    If login info is incorrect, use flask.abort to respond with 401.
    
    Otherwise, create new session for the user, store the session_id as
    a cookie with key "session_id" and returns JSON payload of form.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)
    sesh_id = AUTH.create_session(email)
    result = jsonify({'email': email, 'message': 'logged in'})
    result.set_cookie('session_id', sesh_id)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
