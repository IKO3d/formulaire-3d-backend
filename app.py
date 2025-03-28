from flask_cors import CORS
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
CORS(app)

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json

    email = data.get("email")
    message = data.get("message")
    fichier3d = data.get("fichier3d")
    filename = data.get("filename")

    payload = {
        "service_id": "service_cub2bpl",
        "template_id": "template_4exwh14",
        "user_id": "27iodv7KMIYgP-rUM",
        "template_params": {
            "email": email,
            "message": message,
            "filename": filename,
            "fichier3d": fichier3d
        }
    }

    headers = {"Content-Type": "application/json"}
    res = requests.post("https://api.emailjs.com/api/v1.1/email/send", json=payload, headers=headers)


    if res.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": res.text}), 400

@app.route("/", methods=["GET"])
def index():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
