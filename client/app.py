import requests
from flask import Flask, jsonify, render_template

app = Flask("A Client", template_folder="client/")

api_URL = "http://localhost:8000/"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api", methods=["GET"])
def show():
    response = requests.get(f"{api_URL}/list")
    return jsonify(response.json())


@app.route("/api/<item>", methods=["POST"])
def insert(item):
    response = requests.post(f"{api_URL}/list/{item}")
    return jsonify(response.json())


@app.route("/api", methods=["DELETE"])
def pop():
    response = requests.delete(f"{api_URL}/list")
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
