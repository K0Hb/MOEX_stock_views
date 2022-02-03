from flask import Flask
from flask import request
from flask import jsonify
import os
import requests
from dotenv import load_dotenv
import json

# from flask_sslify import SSLify
# sslify = SSLify(app)

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
URL = f'https://api.telegram.org/bot{TG_TOKEN}/'


def write_json(data, filename='answer'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def send_messages(chat_id, text='Привет'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print('lol')
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message =  r['message']['text']

        if 'sber' in message.lower():
            print('sber')
            send_messages(chat_id, text='цена сбера')
        write_json(r)
        return jsonify(r)
    return '<h1> Hi, i am work. </h1>'


if __name__ == '__main__':
    app.run()

webhook = f'https://api.telegram.org/bot{TG_TOKEN}/setWebhook?url=https://7ae5-62-217-186-124.ngrok.io'