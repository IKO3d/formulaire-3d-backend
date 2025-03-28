from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

EMAILJS_SERVICE_ID = 'service_cub2bpl'
EMAILJS_TEMPLATE_ID = 'template_4exwh14'
EMAILJS_PUBLIC_KEY = '27iodv7KMIYgP-rUM'
EMAILJS_PRIVATE_KEY = 'OpDY_Owi60melSvfAMp8a'

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()

    email = data.get('email')
    message = data.get('message')
    fichier3d = data.get('fichier3d')
    filename = data.get('filename')

    if not email or not message or not fichier3d or not filename:
        return jsonify({'success': False, 'error': 'Missing fields'}), 400

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {EMAILJS_PRIVATE_KEY}'
    }

    payload = {
        "service_id": EMAILJS_SERVICE_ID,
        "template_id": EMAILJS_TEMPLATE_ID,
        "user_id": EMAILJS_PUBLIC_KEY,
        "template_params": {
            "email": email,
            "message": message,
            "fichier3d": fichier3d,
            "filename": filename
        }
    }

    r = requests.post('https://api.emailjs.com/api/v1.0/email/send', headers=headers, json=payload)

    if r.status_code == 200:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': r.text}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
