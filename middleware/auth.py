from flask import request , jsonify,Flask,abort

# Hardcoded token for simplicity
TOKEN = "mysecrettoken"


def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        abort(401,description="Unauthorized")

