import pandas as pd
from flask import (
    Blueprint,
    request,
    jsonify,
)

from models.src.config import (
    BANK_MARKETING_MODEL_VERSION,
    BANK_MARKETING_MODEL_PICKLE,
)
from models.src.helpers import load_model_pipeline
from app.schemas import BANK_MARKETING_MODEL_PARAM_SCHEMA


bank_marketing_bp = Blueprint('bank_marketing_prediction', __name__, url_prefix='/bank_marketing')
BANK_MARKETING_MODEL = load_model_pipeline(BANK_MARKETING_MODEL_PICKLE)


@bank_marketing_bp.route(f'/v{BANK_MARKETING_MODEL_VERSION}/predict', methods=['POST'])
def predict_subscription():
    req_data = request.get_json()
    validated_data = BANK_MARKETING_MODEL_PARAM_SCHEMA.load(req_data)
    if validated_data.errors:
        return jsonify({
            'status': 'error',
            'message': validated_data.errors,
        }), 422

    df = pd.DataFrame([req_data])
    prob = f'{float(BANK_MARKETING_MODEL.predict_proba(df)[:, 1][0]) * 100:.3f}'
    return jsonify({
        'status': 'success',
        'message': f'Likelihood of subscribing to product: {prob} %.',
        'probability': float(prob),
    }), 200
