from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"
EMAILJS_SERVICE_ID = "service_cub2bpl"
EMAILJS_TEMPLATE_ID = "template_4exwh14"
EMAILJS_PUBLIC_KEY = "27iodv7KMIYgP-rUM"

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    print("Payload reçu :", data)

    if not data:
        return jsonify({"success": False, "error": "Aucune donnée reçue"}), 400

    email_data = {
        "service_id": EMAILJS_SERVICE_ID,
        "template_id": EMAILJS_TEMPLATE_ID,
        "user_id": EMAILJS_PUBLIC_KEY,
        "template_params": {
            "email": data.get("email"),
            "message": data.get("message"),
            "filename": data.get("filename"),
            "fichier3d": data.get("fichier3d")
        }
    }

    r = requests.post(EMAILJS_URL, json=email_data)
    print("EmailJS response:", r.status_code, r.text)

    if r.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": r.text}), 400

if __name__ == "__main__":
    app.run(debug=True)
