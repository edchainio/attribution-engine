#!/usr/bin/env python3

import json
import os
import sys

from flask import Flask, jsonify, render_template, request

from extend import authorize


controller = Flask(__name__)

def keymaker(broad, filename='secret_key.dsv'):
    filename = os.path.join(controller.instance_path, filename)
    try:
        broad.config['SECRET_KEY'] = open(filename, "rb").read()
    except IOError:
        absolute_path = os.path.dirname(filename)
        if not os.path.isdir(absolute_path):
            os.system('mkdir -p {absolute_path}'.format(absolute_path=absolute_path))
        os.system('head -c 24 /dev/urando > {filename}'.format(filename=filename))


# Routes for developers in the global scope

@controller.route('/', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'GET':
        return render_template('authenticate.html')
    else:
        pass # TODO

@authorize
@controller.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'GET':
        return render_template('download.html')
    else:
        pass # TODO

@authorize
@controller.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        pass # TODO


# Routes for users in the global scope

@controller.route('/edchain', methods=['GET'])
def edchain():
    pass # FIXME - Return all JSON objects, on edChain

@controller.route('/edchain/books', methods=['GET'])
def edchain_books():
    pass # FIXME - Return a JSON object for every book, on edChain

@controller.route('/edchain/courses', methods=['GET'])
def edchain_courses():
    pass # FIXME - Return a JSON object for every course, on edChain

@controller.route('/edchain/screencasts', methods=['GET'])
def edchain_screencasts():
    pass # FIXME - Return a JSON object for every screencast, on edChain

@controller.route('/edchain/featured/books', methods=['GET'])
def edchain_featured_books():
    pass # FIXME - Return a JSON object for every featured book, on edChain

@controller.route('/edchain/featured/courses', methods=['GET'])
def edchain_featured_courses():
    pass # FIXME - Return a JSON object for every featured course, on edChain

@controller.route('/edchain/featured/screencasts', methods=['GET'])
def edchain_featured_screencasts():
    pass # FIXME - Return a JSON object for every featured screencast, on edChain

@controller.route('/edchain/newest/books', methods=['POST'])
def edchain_newest_books():
    pass # FIXME - Return a JSON object for the n most recently published books, on edChain; where: n is a natural number

@controller.route('/edchain/newest/courses', methods=['POST'])
def edchain_newest_courses():
    pass # FIXME - Return a JSON object for the n most recently published courses, on edChain; where: n is a natural number

@controller.route('/edchain/newest/screencasts', methods=['POST'])
def edchain_newest_screencasts():
    pass # FIXME - Return a JSON object for the n most recently published screencasts, on edChain; where: n is a natural number

@controller.route('/edchain/trending/books', methods=['POST'])
def edchain_trending_books():
    pass # FIXME - Return a JSON object for the n highest rated books over t, on edChain; where: n is a natural number and t is a time period

@controller.route('/edchain/trending/courses', methods=['POST'])
def edchain_trending_courses():
    pass # FIXME - Return a JSON object for the n highest rated courses over t, on edChain; where: n is a natural number and t is a time period

@controller.route('/edchain/trending/screencasts', methods=['POST'])
def edchain_trending_screencasts():
    pass # FIXME - Return a JSON object for the n highest rated courses over t, on edChain; where: n is a natural number and t is a time period


# Routes for users in local scopes

from core.endpoints.group.institution.duke     import handler as duke    
from core.endpoints.group.institution.harvard  import handler as harvard 
from core.endpoints.group.institution.mit      import handler as mit     
from core.endpoints.group.institution.oxford   import handler as oxford  
from core.endpoints.group.institution.stanford import handler as stanford
from core.endpoints.group.institution.yale     import handler as yale    
from core.endpoints.group.endeavor.byte        import handler as byte    
from core.endpoints.group.endeavor.coursera    import handler as coursera
from core.endpoints.group.endeavor.edx         import handler as edx     
from core.endpoints.group.endeavor.lynda       import handler as lynda   
from core.endpoints.group.endeavor.udacity     import handler as udacity 
from core.endpoints.group.endeavor.udemy       import handler as udemy   
from core.endpoints.individual.example         import handler as example

controller.register_blueprint(duke)    
controller.register_blueprint(harvard) 
controller.register_blueprint(mit)     
controller.register_blueprint(oxford)  
controller.register_blueprint(stanford)
controller.register_blueprint(yale)    
controller.register_blueprint(byte)    
controller.register_blueprint(coursera)
controller.register_blueprint(edx)     
controller.register_blueprint(lynda)   
controller.register_blueprint(udacity) 
controller.register_blueprint(udemy)   
controller.register_blueprint(example) 


# Handlers for HTTP status codes in the 4XX error space 

@controller.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "HTTP status code: 400"}), 400)

@controller.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': "HTTP status code: 401"}), 401)

@controller.errorhandler(402)
def payment_required(error):
    return make_response(jsonify({'error': "HTTP status code: 402"}), 402)

@controller.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'error': "HTTP status code: 403"}), 403)

@controller.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "HTTP status code: 404"}), 404)

@controller.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': "HTTP status code: 405"}), 405)

@controller.errorhandler(406)
def not_acceptable(error):
    return make_response(jsonify({'error': "HTTP status code: 406"}), 406)

@controller.errorhandler(407)
def proxy_authentication_required(error):
    return make_response(jsonify({'error': "HTTP status code: 407"}), 407)

@controller.errorhandler(408)
def request_timeout(error):
    return make_response(jsonify({'error': "HTTP status code: 408"}), 408)

@controller.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': "HTTP status code: 409"}), 409)

@controller.errorhandler(410)
def gone(error):
    return make_response(jsonify({'error': "HTTP status code: 410"}), 410)

@controller.errorhandler(411)
def length_required(error):
    return make_response(jsonify({'error': "HTTP status code: 411"}), 411)

@controller.errorhandler(412)
def precondition_failed(error):
    return make_response(jsonify({'error': "HTTP status code: 412"}), 412)

@controller.errorhandler(413)
def payload_too_large(error):
    return make_response(jsonify({'error': "HTTP status code: 413"}), 413)

@controller.errorhandler(414)
def uri_too_long(error):
    return make_response(jsonify({'error': "HTTP status code: 414"}), 414)

@controller.errorhandler(415)
def unsupported_media_types(error):
    return make_response(jsonify({'error': "HTTP status code: 415"}), 415)

@controller.errorhandler(416)
def range_not_satisfiable(error):
    return make_response(jsonify({'error': "HTTP status code: 416"}), 416)

@controller.errorhandler(417)
def expectation_failed(error):
    return make_response(jsonify({'error': "HTTP status code: 417"}), 417)

@controller.errorhandler(418)
def im_a_teapot(error):
    return make_response(jsonify({'error': "HTTP status code: 418"}), 418)

@controller.errorhandler(421)
def misdirected_request(error):
    return make_response(jsonify({'error': "HTTP status code: 421"}), 421)

@controller.errorhandler(422)
def unprocessable_entity(error):
    return make_response(jsonify({'error': "HTTP status code: 422"}), 422)

@controller.errorhandler(423)
def locked(error):
    return make_response(jsonify({'error': "HTTP status code: 423"}), 423)

@controller.errorhandler(424)
def failed_dependency(error):
    return make_response(jsonify({'error': "HTTP status code: 424"}), 424)

@controller.errorhandler(426)
def upgrade_required(error):
    return make_response(jsonify({'error': "HTTP status code: 426"}), 426)

@controller.errorhandler(428)
def precondition_required(error):
    return make_response(jsonify({'error': "HTTP status code: 428"}), 428)

@controller.errorhandler(429)
def too_many_requests(error):
    return make_response(jsonify({'error': "HTTP status code: 429"}), 429)

@controller.errorhandler(431)
def request_header_fields_too_large(error):
    return make_response(jsonify({'error': "HTTP status code: 431"}), 431)

@controller.errorhandler(451)
def unavailable_for_legal_reasons(error):
    return make_response(jsonify({'error': "HTTP status code: 451"}), 451)


# Handlers for HTTP status codes in an unofficial expansion of the 4XX error space 

@controller.errorhandler(444)
def no_response(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 444"}), 444)

@controller.errorhandler(495)
def ssl_certificate_error(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 495"}), 495)

@controller.errorhandler(496)
def ssl_certificate_required(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 496"}), 496)

@controller.errorhandler(497)
def http_request_sent_to_https_port(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 497"}), 497)

@controller.errorhandler(499)
def client_closed_request(error):
    return make_response(jsonify({'error': "Unofficial HTTP status code from Nginx: 499"}), 499)


# Handlers for HTTP status codes in the 5XX error space 

@controller.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': "HTTP status code: 500"}), 500)

@controller.errorhandler(501)
def not_implemented(error):
    return make_response(jsonify({'error': "HTTP status code: 501"}), 501)

@controller.errorhandler(502)
def bad_gateway(error):
    return make_response(jsonify({'error': "HTTP status code: 502"}), 502)

@controller.errorhandler(503)
def service_unavailable(error):
    return make_response(jsonify({'error': "HTTP status code: 503"}), 503)

@controller.errorhandler(504)
def gateway_timeout(error):
    return make_response(jsonify({'error': "HTTP status code: 504"}), 504)

@controller.errorhandler(505)
def http_version_not_supported(error):
    return make_response(jsonify({'error': "HTTP status code: 505"}), 505)

@controller.errorhandler(506)
def variant_also_negotiates(error):
    return make_response(jsonify({'error': "HTTP status code: 506"}), 506)

@controller.errorhandler(507)
def insufficient_storage(error):
    return make_response(jsonify({'error': "HTTP status code: 507"}), 507)

@controller.errorhandler(508)
def loop_detected(error):
    return make_response(jsonify({'error': "HTTP status code: 508"}), 508)

@controller.errorhandler(510)
def not_extended(error):
    return make_response(jsonify({'error': "HTTP status code: 510"}), 510)

@controller.errorhandler(511)
def network_authentication_required(error):
    return make_response(jsonify({'error': "HTTP status code: 511"}), 511)