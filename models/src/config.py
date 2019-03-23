import os

MODELS_PKL_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../models')


BANK_MARKETING_MODEL_VERSION = 1
BANK_MARKETING_MODEL_PICKLE = os.path.join(
    MODELS_PKL_DIR,
    f'bank_marketing_model_v{BANK_MARKETING_MODEL_VERSION}.pkl'
)