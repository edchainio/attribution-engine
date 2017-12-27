#!/usr/bin/env python3

import json

from flask import(
                    Blueprint,
                    jsonify,
                    request)


controller = Blueprint('resources', __name__, url_prefix="/edchain")

@controller.route('/', methods=['GET','POST'])
def get_resources():
    with open('datastore/resources.json', 'r') as file:
        resources = json.load(file)['attributions']
        if request.method == 'GET':
            payload = request.args
        else:
            payload = request.get_json(silent=True)
        if len(payload) < 1:
            return jsonify(resources)
        else:
            # TODO - The following logic should be broken-up into handlers, services, and finders.
            keys = ['content_address', 'copyright_holder', 'course_title', 'instructor_name', 'publication_date', 'subject_matter', 'unique_identifier']
            attributes = []
            for key in payload:
                if key in keys:
                    attributes.append(key)
            attributions = []
            for resource in resources:
                for attribute in attributes:
                    if payload['{key}'.format(key=attribute)] == resource['{key}'.format(key=attribute)]:
                        if 'response_format' not in payload:
                            attributions.append(resource)
                        else:
                            attributions.append(resource['{key}'.format(key=payload['response_format'])])
            if len(attributions) < 1:
                response = {}
            elif len(attributions) == 1:
                response = attributions
            else:
                if isinstance(attributions[0], dict):
                    response = {attribution['unique_identifier']:attribution for attribution in attributions}.values()
                else:
                    response = set(attributions)
            return jsonify(list(response))