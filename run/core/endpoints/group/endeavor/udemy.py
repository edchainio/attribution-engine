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


handler = Blueprint('controller', __name__, url_prefix="/edchain/course/university/udemy")