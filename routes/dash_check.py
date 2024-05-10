import os
import json
from datetime import datetime
from flask import Blueprint, request, jsonify

check_bp = Blueprint('check', __name__)

# Path to the users database file
users_db = os.path.join(os.path.dirname(__file__), '..', 'database', 'users.json')

@check_bp.route('/check', methods=['GET'])
def check_user():
    # Mendapatkan API key dari parameter query string
    api_key = request.args.get('api_key')

    if not api_key:
        return jsonify({"error": "Harap berikan API key"}), 400

    # Membaca data pengguna dari file JSON
    with open(users_db, 'r') as f:
        users = json.load(f)

    # Mendapatkan data pengguna berdasarkan API key
    found_user = None
    for username, user_data in users.items():
        if user_data.get('api_key') == api_key:
            found_user = user_data
            found_user['username'] = username  # Menambahkan nama pengguna ke dalam data

    if found_user:
        # Memeriksa apakah API key telah kedaluwarsa
        expired_date = datetime.strptime(found_user.get('expired_date'), '%d-%m-%Y')
        if expired_date < datetime.now():
            return jsonify({"error": "Apikey Telah Expired"}), 403

        # Menampilkan detail pengguna
        user_details = {
            "Username": found_user.get('username', ''),
            "Email": found_user.get('email', ''),
            "Api_Key": api_key,
            "Expired": found_user.get('expired_date', '')
        }
        return jsonify(user_details), 200
    else:
        return jsonify({"error": "API key tidak valid"}), 404