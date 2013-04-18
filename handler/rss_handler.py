#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" rss_handler.py


"""


import webapp2
from model.file_model import FileModel

class RssHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "application/xml"

        rss = FileModel.read("rss::myhotentry_rss")
        if rss is None:
            rss = ""
        self.response.out.write(rss)
