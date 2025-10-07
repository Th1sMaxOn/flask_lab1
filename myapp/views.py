from datetime import datetime, timezone
from flask import jsonify, request
from . import app

@app.get("/healthcheck")
def healthcheck():
    return jsonify({
        "status": "ok",
        "service": "flask-lab1",
        "time": datetime.now(timezone.utc).isoformat()
    }), 200

@app.get("/hello")
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"}), 200

@app.route("/")
def index():
    return jsonify({"info": "Welcome to Flask Lab 1! Use /hello or /healthcheck"}), 200
