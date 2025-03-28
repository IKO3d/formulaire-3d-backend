from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Autorise les requêtes depuis GitHub Pages

EMAILJS_SERVICE_ID = "service_cub2bpl"
EMAILJS_TEMPLATE_ID = "template_4exwh14"
EMAILJS_PUBLIC_KEY = "27iodv7KMIYgP-rUM"

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()

    required_fields = ["email", "message", "fichier3d", "filename"]
    if not all(field in data for field in required_fields):
        return jsonify({"success": False, "error": "Champs manquants"}), 400

    payload = {
        "service_id": EMAILJS_SERVICE_ID,
        "template_id": EMAILJS_TEMPLATE_ID,
        "user_id": EMAILJS_PUBLIC_KEY,
        "template_params": {
            "email": data["email"],
            "message": data["message"],
            "fichier3d": data["fichier3d"],
            "filename": data["filename"]
        }
    }

    r = requests.post("https://api.emailjs.com/api/v1.0/email/send", json=payload)
    if r.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": r.text}), 400

if __name__ == "__main__":
    app.run(debug=False)
