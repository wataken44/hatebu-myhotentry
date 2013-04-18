#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" index_handler.py


"""

import webapp2
from config import get_config

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        id = get_config()["id"]

        self.response.out.write("""
<!DOCTYPE html>
<html>
<body>
<ul>
<li><a href="/rss">rss<a></li>
<li><a href="http://b.hatena.ne.jp/%s">%s's bookmark</a></li>
<li><a href="https://github.com/wataken44/hatebu-myhotentry">source of this site</a></li>
<li><a href="http://twitter.com/wataken44">@wataken44</a></li>
</body>
</html>
""" % (id, id))
                                
    def head(self):
        pass
