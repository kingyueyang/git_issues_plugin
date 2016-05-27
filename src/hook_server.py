#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    <+ MODULE_NAME +>

    <+ DESCRIPTION +>

    Licensed under the <+ LICENSE +> license, see <+ X +> for more details etc.
    Copyright by yang.yue
'''


import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

