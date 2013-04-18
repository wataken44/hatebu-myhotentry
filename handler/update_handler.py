#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" update_handler.py


"""


import webapp2
import logging

from bs4 import BeautifulSoup
from gaemechanize2._mechanize import Browser

from config import get_config
from model.file_model import FileModel

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
        id = get_config()["id"]
        password = get_config()["password"]

        # login
        browser = Browser()
        browser.open("https://www.hatena.ne.jp/login")
        browser.select_form(nr=0)
        browser["name"] = id
        browser["password"] = password
        browser.submit()

        # html
        browser.open("http://b.hatena.ne.jp/%s/" % id)
        html = browser.response().read()
        
        soup = BeautifulSoup(html)
        link = soup.html.head.find('link', attrs={"rel":"alternate"})
        href = link["href"]

        # rss
        browser.open(href)
        rss = browser.response().read()

        # write to file
        FileModel.write("rss::myhotentry_rss", rss)
