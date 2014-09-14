#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" util.py


"""

import os

def get_abspath(path):
    """ Projectのroot(main.pyのあるディレクトリ)からのpathを受け取り、絶対パスを返す
    
    Args:
        path: (str) path from project root
    Returns: 
        (str) absolute path of |path|
    """
    return os.path.dirname(os.path.abspath(__file__)) + "/" + path
