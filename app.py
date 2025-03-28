from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

EMAILJS_SERVICE_ID = "service_cub2bpl"
EMAILJS_TEMPLATE_ID = "template_4exwh14"
EMAILJS_PUBLIC_KEY = "27iodv7KMIYgP-rUM"

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json

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

    headers = { "Content-Type": "application/json" }

    r = requests.post("https://api.emailjs.com/api/v1.0/email/send", json=payload, headers=headers)

    if r.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": r.text}), 400

@app.route("/")
def index():
    return "OK"
