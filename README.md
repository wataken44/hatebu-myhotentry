hatebu-myhotentry
===============================================

GAEではてなブックマークのMy HotentryのRSSを公開する

つかいかた
----------

    $ git clone git@github.com:wataken44/hatebu-myhotentry.git
    $ cp app-sample.yaml app.yaml
    $ vi app.yaml
      # change wataken44-hatebu-myhotentry -> <your application id>
    $ cp config-sample.json config.json
    $ vi config.json
      # change id/password
    $ appcfg.py . update
