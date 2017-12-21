#!/usr/bin/env python3

import json
import random
import sqlite3
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


handler = Blueprint('controller', __name__, url_prefix="/edchain/course/university/mit")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#                 ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    Endpoints    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#                 ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#                 ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    Version 1    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#                 ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
#
# # This takes a course number and returns an address for content hosted on IPFS
# @handler.route('/content/addresses/<int:course_number>', methods=["GET"])
# def get_content_addresses_by_course_number(course_number):
#     with open('srv/{}/new.json'.format(course_number), "r") as file:
#         document = json.load(file)
#         return document[0]['hash']
#
# # This returns an arbitrary array of courses in lieu of a recommendation system
# @handler.route('/content/addresses/featured', methods=["GET"])
# def get_content_addresses_for_featured_courses():
#     with open('srv/featured/new.json', "r") as file:
#         document = json.load(file)
#         return jsonify(document)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ##

# ...returns a JSON object, which includes the titles and hashes of content, on
# edChain, that is categorized as a course that was published by MIT.
@handler.route('/', methods=['GET', "POST"])
def catchall():
    # Query-string parameters
    #    
    pass

# ...returns a JSON object, which includes the titles and hashes of content, on
# edChain.
@handler.route('/edchain', methods=['GET', "POST"])
def edchain_dump():
    # FIXME
    pass

# ...returns a JSON object, which includes the titles and hashes of content, on 
# edChain, that is categorized as a course.
@handler.route('/edchain/course', methods=['GET', "POST"])
def course_dump():
    # FIXME
    pass

# ...returns a JSON object, which includes the titles and hashes of content, on
# edChain, that is categorized as a course that was published by a university.
@handler.route('/edchain/course/university', methods=['GET', "POST"])
def university_dump():
    # FIXME
    pass

# ...returns a JSON object, which includes the titles and hashes of content, on
# edChain, that is categorized as a course that was published by MIT.
@handler.route('/edchain/course/university/mit', methods=['GET', "POST"])
def mit_dump():
    # FIXME
    pass 


# # ...returns a JSON object, which includes the titles and hashes of content, on
# # edChain, that is categorized as a course that was published by Yale.
# @handler.route('/edchain/course/university/yale', methods=['GET', "POST"])
# def yale_dump():
#     # FIXME
#     pass

# # ...returns a JSON object, which includes the titles and hashes of content, on
# # edChain, that is categorized as a course that was published by Stanford.
# @handler.route('/edchain/course/university/stanford', methods=['GET', "POST"])
# def stanford_dump():
#     # FIXME
#     pass

# # ...returns a JSON object, which includes the titles and hashes of content, on
# # edChain, that is categorized as a course that was published by Harvard.
# @handler.route('/edchain/course/university/harvard', methods=['GET', "POST"])
# def harvard_dump():
#     # FIXME
#     pass

# # ...returns a JSON object, which includes the titles and hashes of content, on
# # edChain, that is categorized as a course that was published by Oxford.
# @handler.route('/edchain/course/university/oxford', methods=['GET', "POST"])
# def oxford_dump():
#     # FIXME
#     pass

# # ...returns a JSON object, which includes the titles and hashes of content, on
# # edChain, that is categorized as a course that was published by Duke.
# @handler.route('/edchain/course/university/duke', methods=['GET', "POST"])
# def duke_dump():
#     # FIXME
#     pass

#
# 
# '/edchain?address={address}'
# '/edchain/course?address={address}'
# '/edchain/course/university?address={address}'
# '/edchain/course/university/mit?address={address}'
#
# 
# '/edchain?identifier={identifier}'
# '/edchain/course?identifier={identifier}'
# '/edchain/course/university?identifier={identifier}'
# '/edchain/course/university/mit?identifier={identifier}'
#
# 
# '/edchain?instructor={instructor}'
# '/edchain/course?instructor={instructor}'
# '/edchain/course/university?instructor={instructor}'
# '/edchain/course/university/mit?instructor={instructor}'
#
# 
# '/edchain?publisher={publisher}'
# '/edchain/course?publisher={publisher}'
# '/edchain/course/university?publisher={publisher}'
# '/edchain/course/university/mit?publisher={publisher}'
#
# 
# '/edchain?title={title}'
# '/edchain/course?title={title}'
# '/edchain/course/university?title={title}'
# '/edchain/course/university/mit?title={title}'
#
# 
# '/edchain?topic={topic}'
# '/edchain/course?topic={topic}'
# '/edchain/course/university?topic={topic}'
# '/edchain/course/university/mit?topic={topic}'

# TODO endpoint that returns an arbitrary number of JSON objects

# TODO featured courses