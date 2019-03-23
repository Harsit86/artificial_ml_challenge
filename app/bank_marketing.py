from flask import Blueprint


from models.src.config import BANK_MARKETING_MODEL_VERSION


bank_marketing_bp = Blueprint('file_upload', __name__, url_prefix='/bank_marketing')


@bank_marketing_bp.route(f'/v{BANK_MARKETING_MODEL_VERSION}/predict', methods=['POST'])
def predict_subscription():
    pass