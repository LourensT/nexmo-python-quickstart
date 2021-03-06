#!/usr/bin/env python3
from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route("/webhooks/message-status", methods=['POST'])
def message_status():
    '''Prints message status and return json status code OK "200" 
    ''' 
    data = request.get_json()
    pprint(data)
    return "200"

if __name__ == '__main__':
    app.run(host="www.example.org", port=3000)
