#!/usr/bin/env python3

import json

from flask import Flask, jsonify


api = Flask(__name__)

@api.route('/content/addresses/<int:course_number>', methods=["GET"])
def get_content_addresses_by_course_number(course_number):
    with open('docstore/{}/new.json'.format(course_number), "r") as file:
        document = json.load(file)
        return document[0]['hash']

@api.route('/content/addresses/featured', methods=["GET"])
def get_content_addresses_for_featured_courses():
#    number_of_featured_courses = 9
#    for featured_course in number_of_featured_courses:
#        print(featured_course)
    print('test')
    with open('docstore/featured/new.json', "r") as file:
        document = json.load(file)
        # print(json.dump(document))
        # print(type(json.dump(document)))
        # return json.dump(document)
        return jsonify(document)



if __name__ == '__main__':
    api.run(host='127.0.0.1', port=5000, debug=True)
#    api.run(host='0.0.0.0', port=5000, debug=True)
