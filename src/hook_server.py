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
from collections import defaultdict

class MainHandler(tornado.web.RequestHandler):
    @property
    def recv_data(self):
        data = defaultdict(lambda : None)
        # 获得所以输入参数,并存在data中
        args = self.request.arguments
        for a in args:
            data[a] = self.get_argument(a)
        # 获取file类型参数
        data["files"] = self.request.files
        # 获取headers
        data["headers"] = self.request.headers

        return data

    def get(self):
        self.render('a.html', title='haha')

    def post(self):
		data = json.loads(self.recv_data["role"])
		data["create time"] = time.strftime("%Y-%m-%d %X")
		self.application.role = data
		print data

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

