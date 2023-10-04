from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form["name"]
        return redirect(url_for("response", user=user))
    return render_template('index.html')


@app.route('/response/<user>', methods=['GET'])
def response(user):
    url = 'https://api.intra.42.fr/oauth/token'
    myobj = {
                'grant_type': os.environ.get("GRANT_TYPE"),
                'client_id' : os.environ.get("CLIENT_ID"),
                'client_secret' : os.environ.get("CLIENT_SECRET")
            }

    x = requests.post(url, json = myobj)
    token = x.json()['access_token']

    endpoint = "https://api.intra.42.fr/v2/users/" + user
    headers = {"Authorization": "Bearer " + token}
    req = requests.get(endpoint, headers=headers)
    return (req.json())
