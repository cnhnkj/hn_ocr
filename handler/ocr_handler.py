import tornado.web
import tornado.gen
import tornado.httpserver
import tornado.escape

from utils.np_encoder import NpEncoder

import time
import json

import logging

logger = logging.getLogger(__name__)


def handler_url(url, coordinate):
    return {'key': 'handler_url', 'url': url, 'coordinate': coordinate}


def handler_file(file, coordinate):
    return {'key': 'handler_file', 'fileName': file.filename, 'coordinate': coordinate}


class OcrRun(tornado.web.RequestHandler):

    def prepare(self):
        super(OcrRun, self).prepare()
        self.json_data = None
        if self.request.body:
            try:
                self.json_data = tornado.escape.json_decode(self.request.body)
            except ValueError as ex:
                logger.error(str(ex))
                pass

    def get_argument(self, arg, default=None, **kwargs):
        if self.request.method in ['POST'] and self.json_data:
            return self.json_data.get(arg, default)
        else:
            return super(OcrRun, self).get_argument(arg, default)

    def get(self):
        self.set_status(405)
        self.finish(json.dumps({'code': 405, 'msg': '目前不支持Get请求'}, cls=NpEncoder))

    @tornado.gen.coroutine
    def post(self):
        url = self.get_argument('url', None)
        coordinate = self.get_argument('coordinate', None)

        file = self.request.files.get('file', None)

        start_time = time.time()
        response = {}
        if url is not None:
            logger.info("request is " + json.dumps({'url': url, 'coordinate': coordinate}))
            response.update(handler_url(url, coordinate))
        elif file is not None and len(file) > 0:
            logger.info("request is " + json.dumps({'file': file[0], 'coordinate': coordinate}))
            response.update(handler_file(file[0], coordinate))
        else:
            self.set_status(400)
            logger.error(json.dumps({'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))
            self.finish(json.dumps({'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))

        response.update({'speed_time': (time.time() - start_time)})
        json_decode = json.dumps({'code': 200, 'msg': '成功', 'data': response}, cls=NpEncoder)

        self.set_status(200)
        self.finish(json_decode)
