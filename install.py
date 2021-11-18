import os

from glob import glob

from cnstd.consts import MODEL_VERSION as CNSTD_MODEL_VERSION
from cnocr.consts import MODEL_VERSION as CNOCR_MODEL_VERSION

from cnstd.utils import get_model_file as std_get_model_file, data_dir as std_data_dir
from cnocr.utils import get_model_file as ocr_get_model_file, data_dir as ocr_data_dir

CN_STD_MODELS = ['db_resnet18', 'db_resnet34', 'db_shufflenet_v2_small', 'db_mobilenet_v3_small']
CN_OCR_MODELS = ['densenet_lite_114-fc', 'densenet_lite_124-fc', 'densenet_lite_134-fc', 'densenet_lite_134-gru',
                 'densenet_lite_136-fc', 'densenet_lite_136-gru']

CNSTD_MODEL_FILE_PREFIX = 'cnstd-v{}'.format(CNSTD_MODEL_VERSION)
CNOCR_MODEL_FILE_PREFIX = 'cnocr-v{}'.format(CNOCR_MODEL_VERSION)


def assert_and_prepare_model_files(root, model_name, cn_std):
    root = os.path.join(root, CNSTD_MODEL_FILE_PREFIX if cn_std is True else CNOCR_MODEL_FILE_PREFIX)
    model_dir = os.path.join(root, model_name)

    model_file_prefix = '{}-{}'.format(CNSTD_MODEL_FILE_PREFIX if cn_std is True else CNOCR_MODEL_FILE_PREFIX,
                                       model_name)
    fps = glob('%s/%s*.ckpt' % (model_dir, model_file_prefix))

    if len(fps) > 1:
        raise ValueError(
            'multiple ckpt files are found in %s, not sure which one should be used'
            % model_dir
        )
    elif len(fps) < 1:
        std_get_model_file(model_dir) if cn_std is True else ocr_get_model_file(model_dir)


def init_cn_std_model():
    for cn_std_model in CN_STD_MODELS:
        assert_and_prepare_model_files(std_data_dir(), cn_std_model, True)


def init_cn_ocr_model():
    for cn_ocr_model in CN_OCR_MODELS:
        assert_and_prepare_model_files(ocr_data_dir(), cn_ocr_model, False)


if __name__ == '__main__':
    init_cn_std_model()
    init_cn_ocr_model()
