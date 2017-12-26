#!/usr/bin/env python3

import json

from flask import(
                    Blueprint,
                    Flask,
                    jsonify,
                    redirect,
                    render_template,
                    request,
                    session,
                    url_for)


controller = Blueprint('content', __name__, url_prefix="/edchain")

@controller.route('/', methods=['GET']) # TODO - Make this route dynamic.
def get_content():
    # Returns attributions for all of the content, on edChain
    with open('attributions/content.json', 'r') as file:
        response = json.load(file)['attributions']
        return jsonify(response)