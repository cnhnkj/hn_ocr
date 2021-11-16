from PIL import ImageDraw


def draw_rectangle(img, box_infos):
    draw_img = ImageDraw.ImageDraw(img)
    for box_info in box_infos['detected_texts']:
        box = box_info['box']
        draw_img.rectangle((int(box[0]), int(box[1]), int(box[2]), int(box[3])), fill=None, outline='red', width=1)
    img.show()
