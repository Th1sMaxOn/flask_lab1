from datetime import datetime, timezone
from flask import Flask, jsonify, request

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
