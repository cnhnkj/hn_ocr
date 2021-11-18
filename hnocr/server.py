import os
import sys

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from settings import config

from cnstd import CnStd
from cnocr import CnOcr

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from hnocr.handler import ocr_url_handler, ocr_file_handler


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self.cn_std = CnStd(model_name=config.cnstd_settings['model_name'],
                            rotated_bbox=config.cnstd_settings['rotated_bbox'])

        self.cn_ocr = CnOcr(model_name=config.cnocr_settings['model_name'],
                            context=config.cnocr_settings['context'])


def make_app():
    tornado.options.options.logging = config.logging_settings['log_level']

    tornado.options.options.log_file_prefix = config.logging_settings['log_path']
    tornado.options.options.log_rotate_mode = config.logging_settings['log_rotate_mode']
    tornado.options.options.log_rotate_when = config.logging_settings['log_rotate_when']
    tornado.options.options.log_rotate_interval = config.logging_settings['log_rotate_interval']

    tornado.options.parse_command_line()

    return Application([
        (r"/api/ocr/url", ocr_url_handler.OcrUrlRun),
        (r"/api/ocr/file", ocr_file_handler.OcrFileRun),
    ])


def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)

    port = config.tornado_settings['port']
    server.bind(port)

    server.start(1)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
