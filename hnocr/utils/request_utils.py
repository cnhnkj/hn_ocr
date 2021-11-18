import requests
import os
import base64

from PIL import Image
from io import BytesIO

import logging

logger = logging.getLogger(__name__)


def find_image(img_src):
    try:
        is_url = img_src.startswith('http:') or img_src.startswith('https:')
        if is_url:
            response = requests.get(img_src)
            if response.ok:
                return Image.open(BytesIO(response.content))
            else:
                return None
        else:
            if os.path.exists(img_src):
                return Image.open(img_src)
            else:
                return None

    except Exception as ex:
        logger.error(str(ex))
        return None


def base64_to_image(image):
    try:
        raw_image = base64.b64decode(image.encode('utf8'))
        img = Image.open(BytesIO(raw_image))
        return img
    except Exception as ex:
        logger.error(str(ex))
        return None
