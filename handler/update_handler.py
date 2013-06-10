#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" update_handler.py


"""

from datetime import datetime, date, timedelta
from time import mktime
import logging
import os

from django.utils import feedgenerator
from google.appengine.ext import db
import webapp2

from feedparser import feedparser
from bs4 import BeautifulSoup
from gaemechanize2._mechanize import Browser

from config import get_config
from model.file_model import FileModel
from model.entry_model import EntryModel

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
        rss = self._get_rss()
        self._parse_and_write_entry(rss)
        self._update_rss()
        self._cleanup_entry()

    def _get_rss(self):
        id = get_config()["id"]
        password = get_config()["password"]

        # login
        browser = Browser()
        browser.open("https://www.hatena.ne.jp/login")
        browser.select_form(nr=0)
        browser["name"] = id
        browser["password"] = password
        browser.submit()

        # rss
        browser.open("http://b.hatena.ne.jp/%s/hotentry.rss" % id)

        return browser.response().read()

    def _parse_and_write_entry(self, raw_rss):
        rss = feedparser.parse(raw_rss)
        
        for entry in rss.entries:
            content = entry.content[0]["value"]
            published = datetime.fromtimestamp(mktime(entry.updated_parsed))
            title = entry.title
            if title is None or title == "":
                title = entry.link

            em = EntryModel.get_or_insert_by_link(
                entry.link,
                link=entry.link, 
                content=content,
                description=entry.description,
                published=published,
                title=title
                )
            # update model
            em.link = entry.link
            em.content = em.content
            em.description = entry.description
            em.published = published
            em.title = title
            em.put()


    def _update_rss(self):
        host = os.environ['HTTP_HOST']
        if host.find('127.0.0.1') >= 0:
            host = host.replace('127.0.0.1', 'localhost')
        
        cfg = get_config()
        id = cfg["id"]

        feed_title = u"%sのマイホットエントリ" % id
        feed_url = "http://%s/rss" % host
        feed_description = feed_title

        feed = feedgenerator.Rss201rev2Feed(
            title = feed_title,
            link = feed_url,
            feed_url = feed_url,
            description = feed_description,
            language = u"ja")

        query = EntryModel.all()
        query.order("-created")
        entries = query.fetch(limit=120)

        for entry in entries:
            feed.add_item(
                title = entry.title,
                link = entry.link,
                unique_id = entry.link,
                description = entry.description,
                pubdate = entry.published)

        FileModel.write("rss::myhotentry_rss", feed.writeString('utf-8'))

    def _cleanup_entry(self):
        old = date.today() - timedelta(3)

        query = EntryModel.all()
        query.filter('created <', old)
        entries = query.fetch(limit=100)

        delete_keys = []
        for entry in entries:
            delete_keys.append(entry.key())

        db.delete(delete_keys)
