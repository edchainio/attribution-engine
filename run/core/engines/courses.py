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


controller = Blueprint('courses', __name__, url_prefix="/edchain/courses")

# Query-string Parameters:
#
# content_address   = payload['content_address']
# copyright_holder  = payload['copyright_holder']
# course_title      = payload['course_title'] 
# instructor_name   = payload['instructor_name']
# publication_date  = payload['publication_date']
# response_format   = payload['response_format']
# subject_matter    = payload['subject_matter']
# unique_identifier = payload['unique_identifier']
#
# print(content_address)
# print(copyright_holder)
# print(course_title)
# print(instructor_name)
# print(publication_date)
# print(response_format)
# print(subject_matter)
# print(unique_identifier)

@controller.route('/', methods=['GET','POST'])
def get_courses(payload=''):
    with open('attributions/courses.json', 'r') as file:
        courses = json.load(file)['attributions']
        if request.method == 'GET':
            payload = request.args
        else:
            payload = request.get_json()
        if len(payload) < 1:
            return jsonify(courses)
        else:
            # TODO - This condition probably needs to be broken-up into, at least, two functions.
            keys = ['content_address', 'copyright_holder', 'course_title', 'instructor_name', 'publication_date', 'subject_matter', 'unique_identifier']
            attributes = []
            for key in payload:
                if key in keys:
                    attributes.append(key)
            attributions = []
            for course in courses:
                for attribute in attributes:
                    if payload['{key}'.format(key=attribute)] == course['{key}'.format(key=attribute)]:
                        if len(payload['response_format']) < 1:
                            attributions.append(course)
                        else:
                            attributions.append(course['{key}'.format(key=payload['response_format'])])
            return jsonify(list(set(attributions)))




# # @controller.route('/featured', methods=['GET'])
# # def get_featured():
# #     # Returns attributions for featured courses, on edChain
# #     pass

# # @controller.route('/most-recent', methods=['GET'])
# # def get_most_recent():
# #     # Returns n attributions for the n most recently published courses, on edChain; where: n is a natural number
# #     pass

# # @controller.route('/most-popular', methods=['GET'])
# # def get_most_popular():
# #     # Returns n attributions for the n highest rated courses over t, on edChain; where: n is a natural number and t is a time period
# #     pass

# @controller.route('/content-address', methods=['GET', 'POST'])
# def get_content_address():
#     payload = request.get_json()
#     if len(payload) == 0:
#         return 'foo'
#     else:
#         return 'bar'
#     # # cruft
#     # if request.method == 'GET':
#     #     # Returns content addresses for some, or all, of the courses, on edChain
#     #     copyright_holder  = request.args.get('copyright-holder')
#     #     course_title      = request.args.get('course-title') # FIXME 1 - also subject to spaces-in-query-string-parameter issue
#     #     instructor_name   = request.args.get('instructor-name') # FIXME 1 - also subject to spaces-in-query-string-parameter issue
#     #     publication_date  = request.args.get('publication-date') # FIXME 1 - This doesn't work well with query-string parameters that have spaces in them.
#     #     subject_matter    = request.args.get('subject-matter') # FIXME 1 - also subject to spaces-in-query-string-parameter issue
#     #     unique_identifier = request.args.get('unique-identifier')
#     #     with open('attributions/courses.json', 'r') as file:
#     #         content_address = []
#     #         rows    = json.load(file)['attributions']
#     #         for row in rows:
#     #             if copyright_holder    == row['copyright_holder']:
#     #                 content_address.append(row['content_address'])
#     #             elif course_title      == row['course_title']:
#     #                 content_address.append(row['content_address'])
#     #             elif instructor_name   == row['instructor_name']:
#     #                 content_address.append(row['content_address'])
#     #             elif publication_date  == row['publication_date']:
#     #                 content_address.append(row['content_address'])
#     #             elif subject_matter    == row['subject_matter']:
#     #                 content_address.append(row['content_address'])
#     #             elif unique_identifier == row['unique_identifier']:
#     #                 content_address.append(row['content_address'])
#     #             else:
#     #                 return jsonify({})
#     #         return jsonify(content_address)
#     # else:
#     #     x = request.get_json()
#     #     print(x)
#     #     return jsonify(x['publication-date'])




# @controller.route('/copyright-holder', methods=['GET'])
# def get_copyright_holder():
#     # Returns copyright holders for some, or all, of the courses, on edChain
#     content_address   = request.args.get('content_address')
#     course_title      = request.args.get('course_title')
#     instructor_name   = request.args.get('instructor_name')
#     publication_date  = request.args.get('publication-date') # FIXME - This doesn't work well with query-string parameters that have spaces in them.
#     subject_matter    = request.args.get('subject_matter')
#     unique_identifier = request.args.get('unique_identifier')
#     with open('attributions/courses.json', 'r') as file:
#         rows = json.load(file)['attributions']
#         for row in rows:
#             if content_address     == row['content_address']:
#                 return jsonify(row['copyright_holder'])
#             elif course_title      == row['course_title']:
#                 return jsonify(row['copyright_holder'])
#             elif instructor_name   == row['instructor_name']:
#                 return jsonify(row['copyright_holder'])
#             elif publication_date  == row['publication_date']:
#                 return jsonify(row['copyright_holder'])
#             elif subject_matter    == row['subject_matter']:
#                 return jsonify(row['copyright_holder'])
#             elif unique_identifier == row['unique_identifier']:
#                 return jsonify(row['copyright_holder'])
#             else:
#                 return jsonify({}) # FIXME - This is a catch-all function so that the tests don't break.

# @controller.route('/course-title', methods=['GET'])
# def get_course_title():
#     # Returns course titles for some, or all, of the courses, on edChain
#     content_address   = request.args.get('content_address')
#     copyright_holder  = request.args.get('copyright_holder')
#     instructor_name   = request.args.get('instructor_name')
#     publication_date  = request.args.get('publication-date') # FIXME - This doesn't work well with query-string parameters that have spaces in them.
#     subject_matter    = request.args.get('subject_matter')
#     unique_identifier = request.args.get('unique_identifier')
#     with open('attributions/courses.json', 'r') as file:
#         rows = json.load(file)['attributions']
#         for row in rows:
#             if content_address     == row['content_address']:
#                 return jsonify(row['course_title'])
#             elif copyright_holder  == row['copyright_holder']:
#                 return jsonify(row['course_title'])
#             elif instructor_name   == row['instructor_name']:
#                 return jsonify(row['course_title'])
#             elif publication_date  == row['publication_date']:
#                 return jsonify(row['course_title'])
#             elif subject_matter    == row['subject_matter']:
#                 return jsonify(row['course_title'])
#             elif unique_identifier == row['unique_identifier']:
#                 return jsonify(row['course_title'])
#             else:
#                 return jsonify({}) # FIXME - This is a catch-all function so that the tests don't break.

# @controller.route('/instructor-name', methods=['GET'])
# def get_instructor_name():
#     # Returns instructor names for some, or all, of the courses, on edChain
#     content_address   = request.args.get('content_address')
#     copyright_holder  = request.args.get('copyright_holder')
#     course_title      = request.args.get('course_title')
#     publication_date  = request.args.get('publication-date') # FIXME - This doesn't work well with query-string parameters that have spaces in them.
#     subject_matter    = request.args.get('subject_matter')
#     unique_identifier = request.args.get('unique_identifier')
#     with open('attributions/courses.json', 'r') as file:
#         rows = json.load(file)['attributions']
#         for row in rows:
#             if content_address     == row['content_address']:
#                 return jsonify(row['instructor_name'])
#             elif copyright_holder  == row['copyright_holder']:
#                 return jsonify(row['instructor_name'])
#             elif course_title      == row['course_title']:
#                 return jsonify(row['instructor_name'])
#             elif publication_date  == row['publication_date']:
#                 return jsonify(row['instructor_name'])
#             elif subject_matter    == row['subject_matter']:
#                 return jsonify(row['instructor_name'])
#             elif unique_identifier == row['unique_identifier']:
#                 return jsonify(row['instructor_name'])
#             else:
#                 return jsonify({}) # FIXME - This is a catch-all function so that the tests don't break.

# @controller.route('/publication-date', methods=['GET'])
# def get_publication_date():
#     # Returns publication dates for some, or all, of the courses, on edChain
#     content_address   = request.args.get('content_address')
#     copyright_holder  = request.args.get('copyright_holder')
#     course_title      = request.args.get('course_title')
#     instructor_name   = request.args.get('instructor_name')
#     subject_matter    = request.args.get('subject_matter')
#     unique_identifier = request.args.get('unique_identifier')
#     with open('attributions/courses.json', 'r') as file:
#         rows = json.load(file)['attributions']
#         for row in rows:
#             if content_address     == row['content_address']:
#                 return jsonify(row['publication_date'])
#             elif copyright_holder  == row['copyright_holder']:
#                 return jsonify(row['publication_date'])
#             elif course_title      == row['course_title']:
#                 return jsonify(row['publication_date'])
#             elif instructor_name   == row['instructor_name']:
#                 return jsonify(row['publication_date'])
#             elif subject_matter    == row['subject_matter']:
#                 return jsonify(row['publication_date'])
#             elif unique_identifier == row['unique_identifier']:
#                 return jsonify(row['publication_date'])
#             else:
#                 return jsonify({}) # FIXME - This is a catch-all function so that the tests don't break.

# @controller.route('/subject-matter', methods=['GET'])
# def get_subject_matter():
#     # Returns subject matter for some, or all, of the courses, on edChain
#     content_address   = request.args.get('content_address')
#     copyright_holder  = request.args.get('copyright_holder')
#     course_title      = request.args.get('course_title')
#     instructor_name   = request.args.get('instructor_name')
#     publication_date  = request.args.get('publication-date') # FIXME - This doesn't work well with query-string parameters that have spaces in them.
#     subject_matter    = request.args.get('subject_matter')
#     unique_identifier = request.args.get('unique_identifier')
#     with open('attributions/courses.json', 'r') as file:
#         rows = json.load(file)['attributions']
#         for row in rows:
#             if content_address     == row['content_address']:
#                 return jsonify(row['subject_matter'])
#             elif copyright_holder  == row['copyright_holder']:
#                 return jsonify(row['subject_matter'])
#             elif course_title      == row['course_title']:
#                 return jsonify(row['subject_matter'])
#             elif instructor_name   == row['instructor_name']:
#                 return jsonify(row['subject_matter'])
#             elif publication_date  == row['publication_date']:
#                 return jsonify(row['subject_matter'])
#             elif unique_identifier == row['unique_identifier']:
#                 return jsonify(row['subject_matter'])
#             else:
#                 return jsonify({}) # FIXME - This is a catch-all function so that the tests don't break.

# @controller.route('/unique-identifier', methods=['GET'])
# def get_unique_identifier():
#     # Returns unique identifiers for some, or all, of the courses, on edChain
#     content_address  = request.args.get('content_address')
#     copyright_holder = request.args.get('copyright_holder')
#     course_title     = request.args.get('course_title')
#     instructor_name  = request.args.get('instructor_name')
#     publication_date  = request.args.get('publication-date') # FIXME - This doesn't work well with query-string parameters that have spaces in them.
#     subject_matter   = request.args.get('subject_matter')
#     with open('attributions/courses.json', 'r') as file:
#         rows = json.load(file)['attributions']
#         for row in rows:
#             if content_address    == row['content_address']:
#                 return jsonify(row['unique_identifier'])
#             elif copyright_holder == row['copyright_holder']:
#                 return jsonify(row['unique_identifier'])
#             elif course_title     == row['course_title']:
#                 return jsonify(row['unique_identifier'])
#             elif instructor_name  == row['instructor_name']:
#                 return jsonify(row['unique_identifier'])
#             elif publication_date == row['publication_date']:
#                 return jsonify(row['unique_identifier'])
#             elif subject_matter   == row['subject_matter']:
#                 return jsonify(row['unique_identifier'])
#             else:
#                 return jsonify({}) # FIXME - This is a catch-all function so that the tests don't break.