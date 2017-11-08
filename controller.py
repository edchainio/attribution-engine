#!/usr/bin/env python3

import json

from flask import Flask, jsonify


api = Flask(__name__)

# This takes a course number and returns an address for content hosted on IPFS
@api.route('/content/addresses/<int:course_number>', methods=["GET"])
def get_content_addresses_by_course_number(course_number):
    with open('srv/{}/new.json'.format(course_number), "r") as file:
        document = json.load(file)
        return document[0]['hash']

# This returns an arbitrary array of courses in lieu of a recommendation system
@api.route('/content/addresses/featured', methods=["GET"])
def get_content_addresses_for_featured_courses():
    with open('srv/featured/new.json', "r") as file:
        document = json.load(file)
        return jsonify(document)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000)
