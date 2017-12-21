#!/usr/bin/env python3

from functools import wraps
from flask import(
					flash,
					g,
					redirect,
					request,
					url_for)


def authorize(endpoint):
	@wraps(endpoint)
		def authorizing(*args, **kwargs):
			if g.username is None:
				flash(u'Please log-in.', 'error')
				return redirect(url_for('core.authenticate', next=request.path))
			return endpoint(*args, **kwargs)
		return authorizing