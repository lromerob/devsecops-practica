from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "context": "DevSecOps Pr?ctica 4",
        "user_mode": "non-root"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
