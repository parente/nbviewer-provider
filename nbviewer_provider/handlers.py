import os

from nbviewer.providers.base import (
    BaseHandler
)
from tornado import (
    gen,
)

class ExampleHandler(BaseHandler):
    @gen.coroutine
    def get(self, page):
        self.write(f'You entered "{page}" on mindtrove.info')
        self.finish()

def default_handlers(handlers=[]):
    return handlers + [
        (r'/example/(?P<page>.*)', ExampleHandler),
    ]

def uri_rewrites(rewrites=[]):
    return rewrites + [
        (r'^http(s?)://mindtrove.info/(.*)$', u'/example/{1}'),
    ]
