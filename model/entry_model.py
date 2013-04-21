#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" entry_model.py


"""

from google.appengine.ext import db 

class EntryModel(db.Model):
    link = db.LinkProperty()
    content = db.TextProperty()
    description = db.TextProperty()
    published = db.DateTimeProperty()
    title = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def build_key(cls, link):
        return "entry-%s" % link

    @classmethod
    def get_by_link(cls, link):
        return cls.get_by_key_name(cls.build_key(link))

    @classmethod
    def get_or_insert_by_link(cls, key_link, **kwds):
        return cls.get_or_insert(cls.build_key(key_link), **kwds)
