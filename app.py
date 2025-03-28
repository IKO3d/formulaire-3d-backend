from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins=["https://iko3d.github.io"])  # ← Très important ici

EMAILJS_SERVICE_ID = "service_cub2bpl"
EMAILJS_TEMPLATE_ID = "template_4exwh14"
EMAILJS_PUBLIC_KEY = "27iodv7KMIYgP-rUM"

@app.route("/send-email", methods=["POST", "OPTIONS"])
def send_email():
    if request.method == "OPTIONS":
        response = jsonify({"ok": True})
        response.headers.add("Access-Control-Allow-Origin", "https://iko3d.github.io")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response

    data = request.get_json()
    if not data:
        return jsonify(success=False, error="Données manquantes")

    payload = {
        "service_id": EMAILJS_SERVICE_ID,
        "template_id": EMAILJS_TEMPLATE_ID,
        "user_id": EMAILJS_PUBLIC_KEY,
        "template_params": {
            "email": data.get("email"),
            "message": data.get("message"),
            "fichier3d": data.get("fichier3d"),
            "filename": data.get("filename")
        }
    }

    r = requests.post("https://api.emailjs.com/api/v1.0/email/send", json=payload)
    if r.status_code == 200:
        return jsonify(success=True)
    else:
        return jsonify(success=False, error=r.text), r.status_code

@app.after_request
def add_cors(response):
    response.headers.add("Access-Control-Allow-Origin", "https://iko3d.github.io")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    return response
