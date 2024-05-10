from flask import Blueprint, jsonify, request
import requests, json, user_agent
from datetime import datetime

useragent_bp = Blueprint('useragent', __name__)

def generate_user_agent():
    ua = user_agent.generate_user_agent()
    return ua

@useragent_bp.route('/user-agent', methods=['GET'])
def generate_random_user_agents():
    num_ua = request.args.get('jum', default=None, type=int)

    if num_ua is None:
        return jsonify({"pembuat": "AmmarBN", "error": "Parameter 'jum' diperlukan."})

    # Logika Anda untuk menghasilkan string user agent secara acak di sini
    user_agents = [generate_user_agent() for _ in range(num_ua)]
    return jsonify({"user_agents": user_agents, "pembuat": "AmmarBN"}), 200
