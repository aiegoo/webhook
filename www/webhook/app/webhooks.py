from flask import request, Blueprint, jsonify, current_app
from ipaddress import ip_address, ip_network
from decouple import config
from git import Repo
import hmac
import requests
import json

webhook = Blueprint('webhook', __name__, url_prefix='')
repo = Repo(config('REPO_PATH'))

@webhook.route('/webhook', methods=['POST'])
def handle_hook():
    #forwarded_for = request.headers.get('X-Forwarded-For')
    #client_ip_address = ip_address(forwarded_for)
    #whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    signature = request.headers.get('X-Hub-Signature')
    sha_name, signature = signature.split('=')

    if sha_name != "sha1":
        return jsonify({'message': 'Invalid sha'}), 501
        
    secret = str.encode(current_app.config.get('GITHUB_SECRET'))
    hashhex = hmac.new(secret, request.data, digestmod=sha_name).hexdigest()
    if not hmac.compare_digest(hashhex, signature):
        return jsonify({'message': 'Invalid signature'}), 403
    
    event = request.headers.get('X-Github-Event', 'ping')
    if event == "ping":
        return jsonify({'message': 'pong'}), 200
    else:
        try:
            origin = repo.remotes.origin
            origin.pull('--rebase')
            return jsonify({'message': 'Repo pulled successfully'}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 403
    return jsonify({}), 204
