from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/send-email": {"origins": "*"}})  # CORS activé

@app.route("/send-email", methods=["OPTIONS", "POST"])
def send_email():
    if request.method == "OPTIONS":
        # Réponse au preflight CORS
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return response

    # Traitement POST classique
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
        response = jsonify({"success": True})
    else:
        response = jsonify({"success": False, "error": res.text})
        response.status_code = 400

    # Ajouter headers CORS à la réponse POST aussi
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/", methods=["GET"])
def index():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
