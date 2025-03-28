from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app, origins="https://iko3d.github.io")  # Autorise ton GitHub Pages uniquement

EMAILJS_SERVICE_ID = "service_cub2bpl"
EMAILJS_TEMPLATE_ID = "template_4exwh14"
EMAILJS_PUBLIC_KEY = "27iodv7KMIYgP-rUM"

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    if not data:
        return jsonify(success=False, error="Pas de données reçues")

    r = requests.post(
        'https://api.emailjs.com/api/v1.0/email/send',
        json={
            'service_id': EMAILJS_SERVICE_ID,
            'template_id': EMAILJS_TEMPLATE_ID,
            'user_id': EMAILJS_PUBLIC_KEY,
            'template_params': {
                'email': data.get('email'),
                'message': data.get('message'),
                'fichier3d': data.get('fichier3d'),
                'filename': data.get('filename')
            }
        },
        headers={'Content-Type': 'application/json'}
    )

    if r.status_code == 200:
        return jsonify(success=True)
    else:
        return jsonify(success=False, error=r.text), r.status_code

# Facultatif : réponse au OPTIONS pour corriger le Preflight CORS
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', 'https://iko3d.github.io')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response
