from marshmallow import (
    Schema,
    fields
)
from marshmallow.validate import (
    OneOf,
    Range,
)

from models.src.data_transformers import MONTH_REPLACE_MAP


VALID_JOBS = [
    'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired',
    'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'
]
VALID_MARTIAL_STATUS = [
    'divorced', 'married', 'single', 'unknown',
]
VALID_EDUCATION = [
    'tertiary', 'secondary', 'unknown', 'primary'
]
VALID_ANSWERS = [
    'no', 'yes', 'unknown',
]
VALID_CONTACTS = [
    'cellular', 'telephone', 'unknown',
]
VALID_POUTCOMES = [
    'failure', 'other', 'success', 'unknown',
]


class BankMarketingModelParamSchema(Schema):

    id = fields.Integer(load_only=True)
    age = fields.Integer(required=True, validate=Range(18, 150))
    job = fields.String(required=True, validate=OneOf(VALID_JOBS))
    marital = fields.String(required=True, validate=OneOf(VALID_MARTIAL_STATUS))
    education = fields.String(required=True, validate=OneOf(VALID_EDUCATION))
    default = fields.String(required=True, validate=OneOf(VALID_ANSWERS))
    balance = fields.Integer(required=True)
    housing = fields.String(required=True, validate=OneOf(VALID_ANSWERS))
    loan = fields.String(required=True, validate=OneOf(VALID_ANSWERS))
    contact = fields.String(required=True, validate=OneOf(VALID_CONTACTS))
    day = fields.Integer(required=True, validate=Range(1, 31))
    month = fields.String(required=True, validate=OneOf(list(MONTH_REPLACE_MAP.keys())))
    duration = fields.Integer(required=True)
    campaign = fields.Integer(required=True)
    pdays = fields.Integer(required=True)
    previous = fields.Integer(required=True)
    poutcome = fields.String(required=True, validate=OneOf(VALID_POUTCOMES))
    y = fields.String(dump_only=True)


BANK_MARKETING_MODEL_PARAM_SCHEMA = BankMarketingModelParamSchema()
