#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" index_handler.py


"""

import webapp2

from config import get_config
from handler.base_handler import BaseHandler
from model.file_model import FileModel

class IndexHandler(BaseHandler):
    def get(self):
        id = get_config()["id"]
        entries = FileModel.read("json::myhotentry_rss")
        if entries == None:
            entries = []

        context = {
            "id": id,
            "entries": entries
        }

        self.response.out.write(self._render('index.html', context))
                                
    def head(self):
        pass
