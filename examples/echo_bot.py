# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return 'Welcome to echo bot server!'

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["시작하기", "도움말"]
    }

    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    echo = "Echo : " + content
    dataSend = {
        "message" : {
            "text" : echo
        }
    }
    print(echo)
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)