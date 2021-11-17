import tornado.gen
import tornado.escape

import time
import json

import logging

from PIL import Image
from io import BytesIO

from handler.base_handler import BaseHandler

from utils.np_encoder import NpEncoder

logger = logging.getLogger(__name__)


class OcrFileRun(BaseHandler):

    def get(self):
        self.set_status(405)
        self.finish(json.dumps({'code': 405, 'msg': '目前不支持Get请求'}, cls=NpEncoder))

    @tornado.gen.coroutine
    def post(self):
        coordinate = True if (self.get_argument('coordinate', '').lower() == 'true') else False
        file = self.request.files.get('file', None)

        start_time = time.time()
        response = {}
        try:
            if file is not None and len(file) > 0:
                response.update(self.handler_file(file[0], coordinate))
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

    def handler_file(self, file, coordinate):
        img = Image.open(BytesIO(file.body))

        if img is None:
            raise RuntimeError("上传文件解析失败")

        return self.analysis_file(img, coordinate)
