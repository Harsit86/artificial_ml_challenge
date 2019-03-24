import pandas as pd
from flask import (
    Blueprint,
    request,
    jsonify,
)
from marshmallow.exceptions import ValidationError


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
    try:
        data = BANK_MARKETING_MODEL_PARAM_SCHEMA.load(req_data)
    except ValidationError as exc:
        return jsonify({
            'status': 'error',
            'message': exc.messages
        }), 422

    df = pd.DataFrame([req_data])
    prob = f'{float(BANK_MARKETING_MODEL.predict_proba(df)[:, 1][0]) * 100:.3f}'
    return jsonify({
        'status': 'success',
        'message': f'Likelihood of subscribing to product: {prob} %.',
        'probability': float(prob),
    }), 200
