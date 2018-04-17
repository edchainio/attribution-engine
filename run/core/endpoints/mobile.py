#!/usr/bin/env python3

import json

from flask import(
                    Blueprint,
                    jsonify,
                    request)


controller = Blueprint('mobile', __name__, url_prefix="/edchain/mobile")

@controller.route('/', methods=['GET','POST'])
def get_mobile():
    with open('datastore/mini_yale_courses.json', 'r') as file:
        mobile = json.load(file)['attributions']
        if request.method == 'GET':
            payload = request.args
        else:
            payload = request.get_json(silent=True)
        if payload is None:
            return jsonify(list({}))
        elif len(payload) < 1:
            return jsonify(mobile)
        else:
            # TODO - The following logic should be broken-up into handlers, services, and finders.
            keys = ['content_address', 'copyright_holder', 'course_title', 'instructor_name', 'publication_date', 'subject_matter', 'unique_identifier']
            attributes = []
            for key in payload:
                if key in keys:
                    attributes.append(key)
            attributions = []
            for course in mobile:
                for attribute in attributes:
                    if course['{key}'.format(key=attribute)] == payload['{key}'.format(key=attribute)]:
                        if 'response_subtype' in payload:
                            attributions.append(course['{key}'.format(key=payload['response_subtype'])])
                        else:
                            attributions.append(course)
            if len(attributions) < 1:
                response = {}
            elif len(attributions) == 1:
                response = attributions
            else:
                if isinstance(attributions[0], dict):
                    response = {attribution['unique_identifier']:attribution for attribution in attributions}.values()
                else:
                    response = set(attributions)
        if 'response_size' in payload:
            return jsonify(list(response)[:int('{limit}'.format(limit=payload['response_size']))])
        else:
            return jsonify(list(response))
