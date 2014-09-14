#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py


"""

import webapp2

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')

from config import load_config
from handler.rss_handler import RssHandler
from handler.index_handler import IndexHandler
from handler.update_handler import UpdateHandler

load_config()

application = webapp2.WSGIApplication([
        ('/rss', RssHandler),
        ('/', IndexHandler),
        ('^/update/(.*)$', UpdateHandler),
        ])
