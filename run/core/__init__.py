#!/usr/bin/env python3

import json
import os
import random
import sys
import time

from flask import Flask, jsonify, render_template, request

from extend import authorize


omnibus = Flask(__name__)

def keymaker(broad, filename='secret_key.dsv'):
    filename = os.path.join(omnibus.instance_path, filename)
    try:
        broad.config['SECRET_KEY'] = open(filename, "rb").read()
    except IOError:
        absolute_path = os.path.dirname(filename)
        if not os.path.isdir(absolute_path):
            os.system('mkdir -p {absolute_path}'.format(absolute_path=absolute_path))
        os.system('head -c 24 /dev/urando > {filename}'.format(filename=filename))


# Routes for requests related to the node

@omnibus.route('/', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'GET':
        return render_template('authenticate.html')
    else:
        pass # TODO

@authorize
@omnibus.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'GET':
        return render_template('download.html')
    else:
        pass # TODO

@authorize
@omnibus.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        pass # TODO


# Routes for requests related to the network

@omnibus.route('/edchain', methods=['GET'])
def edchain():
    pass # FIXME - Return all JSON objects, on edChain

@omnibus.route('/edchain/books', methods=['GET'])
def edchain_books():
    pass # TODO - Return a JSON object for every book, on edChain

@omnibus.route('/edchain/courses', methods=['GET'])
def edchain_courses():
    pass # FIXME - Return a JSON object for every course, on edChain

@omnibus.route('/edchain/screencasts', methods=['GET'])
def edchain_screencasts():
    pass # TODO - Return a JSON object for every screencast, on edChain

@omnibus.route('/edchain/featured/books', methods=['GET'])
def edchain_featured_books():
    pass # TODO - Return a JSON object for every featured book, on edChain

@omnibus.route('/edchain/featured/courses', methods=['GET'])
def edchain_featured_courses():
    pass # TODO - Return a JSON object for every featured course, on edChain

@omnibus.route('/edchain/featured/screencasts', methods=['GET'])
def edchain_featured_screencasts():
    pass # TODO - Return a JSON object for every featured screencast, on edChain

@omnibus.route('/edchain/newest/books', methods=['POST'])
def edchain_newest_books():
    pass # TODO - Return a JSON object for the n most recently published books, on edChain; where: n is a natural number

@omnibus.route('/edchain/newest/courses', methods=['POST'])
def edchain_newest_courses():
    pass # TODO - Return a JSON object for the n most recently published courses, on edChain; where: n is a natural number

@omnibus.route('/edchain/newest/screencasts', methods=['POST'])
def edchain_newest_screencasts():
    pass # TODO - Return a JSON object for the n most recently published screencasts, on edChain; where: n is a natural number

@omnibus.route('/edchain/trending/books', methods=['POST'])
def edchain_trending_books():
    pass # TODO - Return a JSON object for the n highest rated books over t, on edChain; where: n is a natural number and t is a time period

@omnibus.route('/edchain/trending/courses', methods=['POST'])
def edchain_trending_courses():
    pass # TODO - Return a JSON object for the n highest rated courses over t, on edChain; where: n is a natural number and t is a time period

@omnibus.route('/edchain/trending/screencasts', methods=['POST'])
def edchain_trending_screencasts():
    pass # TODO - Return a JSON object for the n highest rated courses over t, on edChain; where: n is a natural number and t is a time period


# Blueprints for queries

from core.controllers.courses import controller as course

omnibus.register_blueprint(course)


# Error handlers for HTTP status codes in the 4XX error-space

@omnibus.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "HTTP status code: 400"}), 400)

@omnibus.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': "HTTP status code: 401"}), 401)

@omnibus.errorhandler(402)
def payment_required(error):
    return make_response(jsonify({'error': "HTTP status code: 402"}), 402)

@omnibus.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'error': "HTTP status code: 403"}), 403)

@omnibus.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "HTTP status code: 404"}), 404)

@omnibus.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': "HTTP status code: 405"}), 405)

@omnibus.errorhandler(406)
def not_acceptable(error):
    return make_response(jsonify({'error': "HTTP status code: 406"}), 406)

@omnibus.errorhandler(407)
def proxy_authentication_required(error):
    return make_response(jsonify({'error': "HTTP status code: 407"}), 407)

@omnibus.errorhandler(408)
def request_timeout(error):
    return make_response(jsonify({'error': "HTTP status code: 408"}), 408)

@omnibus.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': "HTTP status code: 409"}), 409)

@omnibus.errorhandler(410)
def gone(error):
    return make_response(jsonify({'error': "HTTP status code: 410"}), 410)

@omnibus.errorhandler(411)
def length_required(error):
    return make_response(jsonify({'error': "HTTP status code: 411"}), 411)

@omnibus.errorhandler(412)
def precondition_failed(error):
    return make_response(jsonify({'error': "HTTP status code: 412"}), 412)

@omnibus.errorhandler(413)
def payload_too_large(error):
    return make_response(jsonify({'error': "HTTP status code: 413"}), 413)

@omnibus.errorhandler(414)
def uri_too_long(error):
    return make_response(jsonify({'error': "HTTP status code: 414"}), 414)

@omnibus.errorhandler(415)
def unsupported_media_types(error):
    return make_response(jsonify({'error': "HTTP status code: 415"}), 415)

@omnibus.errorhandler(416)
def range_not_satisfiable(error):
    return make_response(jsonify({'error': "HTTP status code: 416"}), 416)

@omnibus.errorhandler(417)
def expectation_failed(error):
    return make_response(jsonify({'error': "HTTP status code: 417"}), 417)

@omnibus.errorhandler(418)
def im_a_teapot(error):
    return make_response(jsonify({'error': "HTTP status code: 418"}), 418)

@omnibus.errorhandler(421)
def misdirected_request(error):
    return make_response(jsonify({'error': "HTTP status code: 421"}), 421)

@omnibus.errorhandler(422)
def unprocessable_entity(error):
    return make_response(jsonify({'error': "HTTP status code: 422"}), 422)

@omnibus.errorhandler(423)
def locked(error):
    return make_response(jsonify({'error': "HTTP status code: 423"}), 423)

@omnibus.errorhandler(424)
def failed_dependency(error):
    return make_response(jsonify({'error': "HTTP status code: 424"}), 424)

@omnibus.errorhandler(426)
def upgrade_required(error):
    return make_response(jsonify({'error': "HTTP status code: 426"}), 426)

@omnibus.errorhandler(428)
def precondition_required(error):
    return make_response(jsonify({'error': "HTTP status code: 428"}), 428)

@omnibus.errorhandler(429)
def too_many_requests(error):
    return make_response(jsonify({'error': "HTTP status code: 429"}), 429)

@omnibus.errorhandler(431)
def request_header_fields_too_large(error):
    return make_response(jsonify({'error': "HTTP status code: 431"}), 431)

@omnibus.errorhandler(451)
def unavailable_for_legal_reasons(error):
    return make_response(jsonify({'error': "HTTP status code: 451"}), 451)


# Error handlers for HTTP status codes in an unofficial expansion of the 4XX error-space

@omnibus.errorhandler(444)
def no_response(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 444"}), 444)

@omnibus.errorhandler(495)
def ssl_certificate_error(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 495"}), 495)

@omnibus.errorhandler(496)
def ssl_certificate_required(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 496"}), 496)

@omnibus.errorhandler(497)
def http_request_sent_to_https_port(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 497"}), 497)

@omnibus.errorhandler(499)
def client_closed_request(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 499"}), 499)


# Error handlers for HTTP status codes in the 5XX error-space

@omnibus.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': "HTTP status code: 500"}), 500)

@omnibus.errorhandler(501)
def not_implemented(error):
    return make_response(jsonify({'error': "HTTP status code: 501"}), 501)

@omnibus.errorhandler(502)
def bad_gateway(error):
    return make_response(jsonify({'error': "HTTP status code: 502"}), 502)

@omnibus.errorhandler(503)
def service_unavailable(error):
    return make_response(jsonify({'error': "HTTP status code: 503"}), 503)

@omnibus.errorhandler(504)
def gateway_timeout(error):
    return make_response(jsonify({'error': "HTTP status code: 504"}), 504)

@omnibus.errorhandler(505)
def http_version_not_supported(error):
    return make_response(jsonify({'error': "HTTP status code: 505"}), 505)

@omnibus.errorhandler(506)
def variant_also_negotiates(error):
    return make_response(jsonify({'error': "HTTP status code: 506"}), 506)

@omnibus.errorhandler(507)
def insufficient_storage(error):
    return make_response(jsonify({'error': "HTTP status code: 507"}), 507)

@omnibus.errorhandler(508)
def loop_detected(error):
    return make_response(jsonify({'error': "HTTP status code: 508"}), 508)

@omnibus.errorhandler(510)
def not_extended(error):
    return make_response(jsonify({'error': "HTTP status code: 510"}), 510)

@omnibus.errorhandler(511)
def network_authentication_required(error):
    return make_response(jsonify({'error': "HTTP status code: 511"}), 511)
