#!/usr/bin/env python3

import csv
import json
import random
import time

from flask import(
                    Blueprint,
                    Flask,
                    jsonify,
                    redirect,
                    render_template,
                    request,
                    session,
                    url_for)


controller = Blueprint('controller', __name__, url_prefix="/edchain/course")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#                 ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    Version 1    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#                 ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#
# # This takes a course number and returns an address for content hosted on IPFS
# @controller.route('/content/addresses/<int:course_number>', methods=["GET"])
# def get_content_addresses_by_course_number(course_number):
#     with open('srv/{}/new.json'.format(course_number), "r") as file:
#         document = json.load(file)
#         return document[0]['hash']
#
# # This returns an arbitrary array of courses in lieu of a recommendation system
# @controller.route('/content/addresses/featured', methods=["GET"])
# def get_content_addresses_for_featured_courses():
#     with open('srv/featured/new.json', "r") as file:
#         document = json.load(file)
#         return jsonify(document)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##


@controller.route('/mit', methods=['GET'])
def mit():

    # pass # FIXME - Return all JSON objects, by MIT, on edChain

    content_address   = request.args.get('content_address')
    copyright_holder  = request.args.get('copyright_holder')
    course_title      = request.args.get('course_title')
    instructor_name   = request.args.get('instructor_name')
    publication_date  = request.args.get('publication_date')
    subject_matter    = request.args.get('subject_matter')
    unique_identifier = request.args.get('unique_identifier')

    with open('datastore/mit.json', 'r') as file:
        rows = json.load(file)['courses']
        for row in rows:
            if content_address == row['content_address']:
                return jsonify(row)
            else:
                pass
