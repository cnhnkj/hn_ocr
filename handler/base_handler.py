import tornado.web
import tornado.escape

import logging

logger = logging.getLogger(__name__)


class BaseHandler(tornado.web.RequestHandler):

    @property
    def cn_std(self):
        return self.application.cn_std

    @property
    def cn_ocr(self):
        return self.application.cn_ocr

    def prepare(self):
        super(BaseHandler, self).prepare()
        self.json_data = None
        if self.request.body:
            try:
                self.json_data = tornado.escape.json_decode(self.request.body)
            except ValueError as ex:
                logger.error(str(ex))
                pass

    def get_argument(self, arg, default=None, **kwargs):
        if self.request.method in ['POST'] and self.request.headers['Content-Type'].startswith(
                'application/json') and self.json_data:
            return self.json_data.get(arg, default)
        else:
            return super(BaseHandler, self).get_argument(arg, default)

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def analysis_file(self, img, coordinate):
        box_infos = self.cn_std.detect(img)
        ocr_res = self.img_ocr(box_infos)
        if coordinate is not True:
            for res in ocr_res:
                res.pop('ocr_box')

        return {'ocr_res': ocr_res}

    def img_ocr(self, box_infos):
        ocr_res = []
        for box_info in box_infos['detected_texts']:
            cropped_img = box_info['cropped_img']
            box = box_info['box']
            words, prob = self.cn_ocr.ocr_for_single_line(cropped_img)
            ocr_res.append({'ocr_result': ''.join(words), 'ocr_prob': prob, 'ocr_box': box})

        # 按坐标y,x进行排序
        return sorted(ocr_res, key=lambda res: (res['ocr_box'][1], res['ocr_box'][0]))
