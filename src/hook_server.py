#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    <+ MODULE_NAME +>

    <+ DESCRIPTION +>

    Licensed under the <+ LICENSE +> license, see <+ X +> for more details etc.
    Copyright by yang.yue
'''

import json
import time

import tornado.web
import tornado.ioloop
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.get_argument('body', 'No data received')
        self.write(data)
        print self.request.arguments

    def get(self):
        self.write("Hello, world")

class GitlabIssues(tornado.web.RequestHandler):
    def post(self):
        data = self.get_argument('body', 'No data received')
        self.write(data)
        print self.request.arguments

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/gitlab/issues', GitlabIssues),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

