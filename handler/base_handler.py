#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" base_handler.py


"""

import jinja2
import webapp2

import util

class BaseHandler(webapp2.RequestHandler):
    def __init__(self, *args, **kwargs):
        webapp2.RequestHandler.__init__(self, *args, **kwargs)

        print(util.get_abspath("template"))

        self.__env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(util.get_abspath("template")),
            extensions=['jinja2.ext.autoescape'],
            autoescape=False)

    def _render(self, name, context):
        template = self.__env.get_template(name)
        return template.render(context)

if __name__ == "__main__":
    pass
