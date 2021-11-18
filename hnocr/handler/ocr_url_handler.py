import tornado.gen
import tornado.escape

import time
import json

import logging

from hnocr.utils.np_encoder import NpEncoder
from hnocr.utils import request_utils

from hnocr.handler.base_handler import BaseHandler



logger = logging.getLogger(__name__)


class OcrUrlRun(BaseHandler):

    def get(self):
        self.set_status(405)
        self.finish(json.dumps({'code': 405, 'msg': '目前不支持Get请求'}, cls=NpEncoder))

    @tornado.gen.coroutine
    def post(self):
        url = self.get_argument('url', None)
        coordinate = self.get_argument('coordinate', '')

        start_time = time.time()
        response = {}
        try:
            if url is not None:
                logger.info("request is " + json.dumps({'url': url, 'coordinate': coordinate}))
                response.update(self.handler_url(url, coordinate))
            else:
                self.set_status(400)
                logger.error(json.dumps({'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))
                self.finish(json.dumps({'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))
        except RuntimeError as ex:
            error_log = json.dumps({'code': 400, 'msg': str(ex)}, cls=NpEncoder)
            logger.error(error_log, exc_info=True)
            self.finish(error_log)
            return

        response.update({'speed_time': (time.time() - start_time)})
        json_decode = json.dumps({'code': 200, 'msg': '成功', 'data': response}, cls=NpEncoder)
        logger.info(json_decode)

        self.set_status(200)
        self.finish(json_decode)

    def handler_url(self, url, coordinate):
        img = request_utils.find_image(url)

        if img is None:
            raise RuntimeError("图片下载失败，请确认图片路径正确性")

        return self.analysis_file(img, coordinate)


