#!/usr/bin/env python3

import json

from flask import Flask


api = Flask(__name__)

@api.route('/content/addresses/<int:course_number>', methods=["GET"])
def get_content_addresses_by_course_number(course_number):
    with open('docstore/{}/new.json'.format(course_number), "r") as file:
        document = json.load(file)
        return document[0]['hash']

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=5000, debug=True)
