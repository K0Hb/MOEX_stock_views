from asyncore import write
from flask import Flask
from flask import request
from flask import jsonify
import os
import requests
from dotenv import load_dotenv
import json

# from flask_sslify import SSLify

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
URL = f'https://api.telegram.org/bot{TG_TOKEN}/'

 
# sslify = SSLify(app)

def write_json(data, filename='answer'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_updates():
    url = URL + 'getUpdates'
    r= requests.get(url)
    # write_json(r.json())
    return r.json()

def send_messages(chat_id, text='Привет'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

def main():
    r = requests.get(URL + 'getMe')
    write_json(r.json())
    pass

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        write_json(r)
        return jsonify(r)
    return '<h1> Hi, i am work. </h1>'


if __name__ == '__main__':
    # r = get_updates()
    # chat_id = r['result'][-1]['message']['chat']['id']
    # send_messages(chat_id)
    app.run()

webhook = f'https://api.telegram.org/bot{TG_TOKEN}/setWebhook?url=https://dfb5-62-217-186-124.ngrok.io/'