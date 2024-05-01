# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the API"

@app.route("/customers", methods=["GET"])
def get_customers():
    # Example endpoint to return some customer data
    data = {
        "customers": [
            {"id": 1, "name": "John Doe", "email": "john@example.com"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
        ]
    }
    return jsonify(data)

@app.route("/purchases", methods=["GET"])
def get_purchases():
    # Example endpoint to return some purchase data
    data = {
        "purchases": [
            {"id": 1, "customer_id": 1, "item": "Laptop", "price": 1200},
            {"id": 2, "customer_id": 2, "item": "Tablet", "price": 300},
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
