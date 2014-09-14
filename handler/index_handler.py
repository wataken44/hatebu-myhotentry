#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" index_handler.py


"""

import webapp2

from config import get_config
from handler.base_handler import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        id = get_config()["id"]

        context = {
            "id": id,
            "links": [
                {
                    "href": "http://www.goo.ne.jp/",
                    "title": "goo"
                },
                {
                    "href": "http://www.yahoo.co.jp/",
                    "title": "yahoo"
                },
            ]
        }

        self.response.out.write(self._render('index.html', context))
                                
    def head(self):
        pass
