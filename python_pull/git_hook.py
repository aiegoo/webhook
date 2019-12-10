from flask import Flask, request
import json
import hmac
import os
import subprocess
import hashlib

app = Flask(__name__)

SECRET_KEY = os.getenv('WEBHOOK_SECRET_KEY')

def validate_signature(data):
    sha_name, signature = request.headers['X-Hub-Signature'].split('=')
    if sha_name != 'sha1':
        return False

    mac = hmac.new(str(SECRET_KEY), msg=str(data), digestmod=hashlib.sha1)
    return hmac.compare_digest(mac.hexdigest(), str(signature))

@app.route('/payload/<repo_name>',methods=['POST'])
def foo(repo_name):
#  data = json.loads(request.data)
   #print (data)
#  flag = validate_signature(request.data)
   #print(flag)
   subprocess.call(["/root/repos/python_pull/git_pull.sh", repo_name])
   return "OK"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)
