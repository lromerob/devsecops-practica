from flask import Flask, jsonify
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

VAULT_NAME = "kv-devsecops"
KEY_VAULT_URL = f"https://{VAULT_NAME}.vault.azure.net/"

def obtener_secreto_seguro():
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
        secret = client.get_secret("DB-CONNECTION")
        return secret.value
    except Exception as e:
        return "Simulado: Server=localhost;User=appuser;Password=LocalSecurePass123!"

@app.route('/')
def home():
    secreto_recuperado = obtener_secreto_seguro()
    return jsonify({
        "status": "running",
        "context": "DevSecOps Pr?ctica 4 - Final",
        "user_mode": "non-root",
        "key_vault_target": VAULT_NAME,
        "database_secret": secreto_recuperado
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
