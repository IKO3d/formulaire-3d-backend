from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

@app.route("/send-email", methods=["POST", "OPTIONS"])
def send_email():
    if request.method == "OPTIONS":
        return '', 204  # Répond au preflight

    data = request.json

    payload = {
        "service_id": "service_cub2bpl",
        "template_id": "template_4exwh14",
        "user_id": "27iodv7KMIYgP-rUM",
        "template_params": {
            "email": data.get("email"),
            "message": data.get("message"),
            "filename": data.get("filename"),
            "fichier3d": data.get("fichier3d")
        }
    }

    headers = {"Content-Type": "application/json"}
    r = requests.post("https://api.emailjs.com/api/v1.1/email/send", json=payload, headers=headers)

    if r.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": r.text}), 400

@app.route("/", methods=["GET"])
def index():
    return "Backend OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
