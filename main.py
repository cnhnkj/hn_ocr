from cnstd import CnStd

from utils import std_utils, request_utils

from cnocr import CnOcr


def img_ocr(cn_ocr, box_infos):
    ocr_res = []
    for box_info in box_infos['detected_texts']:
        cropped_img = box_info['cropped_img']
        ocr_res.append(cn_ocr.ocr_for_single_line(cropped_img))
    return ocr_res


if __name__ == '__main__':
    std = CnStd(rotated_bbox=False)
    cn_ocr = CnOcr(model_name='densenet_lite_136-gru')
    # img_arr = ['examples/address_001.png', 'https://image.cnhnb.com/image/jpg/head/2021/10/31/ebb000315807439cb92bcde5dc9136ce.jpg', 'examples/taobao.jpeg']
    img_arr = ['examples/shouxie_001.png', 'examples/shouxie_002.png', 'examples/shouxie_003.jpeg', 'examples/shouxie_004.png']

    for img_url in img_arr:
        img = request_utils.find_image(img_url)

        if img is None:
            print("img_url[%s]错误", img_url)
            continue

        box_infos = std.detect(img)
        # std_utils.draw_rectangle(img, box_infos)
        ocr_res = img_ocr(cn_ocr, box_infos)
        print('ocr result: %s' % str(ocr_res))

