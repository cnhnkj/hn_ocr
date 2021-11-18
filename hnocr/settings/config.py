import os

BASE_DIRS = os.path.dirname(__file__)

logging_settings = {'log_path': os.path.join(os.path.dirname(__file__), "../../logs/log.log"),
                    'log_level': 'debug',
                    'log_rotate_mode': 'time',
                    'log_rotate_when': 'D',
                    'log_rotate_interval': 1}

tornado_settings = {'port': 8898}

cnstd_settings = {
    'model_name': 'db_shufflenet_v2_small',
    'rotated_bbox': False
}

cnocr_settings = {
    'model_name': 'densenet_lite_136-gru',
    'context': 'cpu'
}
