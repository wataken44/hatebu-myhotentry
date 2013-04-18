#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" config.py
Application Configuration 

"""

import json

config = None

def load_config(filename = "config.json"):
    global config
    fp = open(filename)
    config = json.loads(fp.read(), "UTF-8")
    fp.close()

def get_config():
    global config
    return config
