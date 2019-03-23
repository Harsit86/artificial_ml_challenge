from flask import Blueprint


from models.src.config import (
    BANK_MARKETING_MODEL_VERSION,
    BANK_MARKETING_MODEL_PICKLE,
)
from models.src.helpers import load_model_pipeline


bank_marketing_bp = Blueprint('bank_marketing_prediction', __name__, url_prefix='/bank_marketing')
model = load_model_pipeline(BANK_MARKETING_MODEL_PICKLE)


@bank_marketing_bp.route(f'/v{BANK_MARKETING_MODEL_VERSION}/predict', methods=['POST'])
def predict_subscription():
    pass