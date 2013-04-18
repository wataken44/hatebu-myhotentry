#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" file_model.py
File class which saves it's content into DataStore

"""

import pickle
from google.appengine.ext import db 

class FileModel(db.Model):
    name = db.StringProperty()
    text = db.BlobProperty()

    @classmethod
    def build_key(cls, name):
        return "file-%s" % name

    @classmethod
    def get_by_name(cls, name):
        return cls.get(cls.build_key(name))

    @classmethod
    def read(cls, name):
        key = cls.build_key(name)
        model = cls.get_or_insert(key, name=name, text=pickle.dumps(None))
        return pickle.loads(model.text)

    @classmethod
    def write(cls, name, content):
        key = cls.build_key(name)
        model = cls(key_name=key, name=name, text=pickle.dumps(content))
        model.put()

if __name__ == "__main__":
    pass
