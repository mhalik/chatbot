# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 20:50:29 2017

@author: Max
"""

from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAADgJ894XckBAAo3sXg6DOYgpQabVDzVoLGT43KZAwvIM59iBgvchbGKQq5YAvpN4rGAuZBMa5DnozzszdMZBNCZBjLPrpi2PTwJQWXmOkLbX7XbcMXxY50yOimwJLZCBeneGNzuy7gdSfG4GFwxkxmJCLnZBhnl5DzEcHsDtdvwZDZD"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message[::-1])
    return "ok"

@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge','']

    
if __name__ == '__main__':
    app.run(debug=True)