from marshmallow import (
    Schema,
    fields
)


class BankMarketingModelParamSchema(Schema):

    age = fields.Integer(required=True)
    job = fields.String(required=True)
    marital = fields.String(required=True)
    education = fields.String(required=True)
    default = fields.String(required=True)
    balance = fields.Integer(required=True)
    housing = fields.String(required=True)
    loan = fields.String(required=True)
    contact = fields.String(required=True)
    day = fields.Integer(required=True)
    month = fields.String(required=True)
    duration = fields.Integer(required=True)
    campaign = fields.Integer(required=True)
    pdays = fields.Integer(required=True)
    previous = fields.Integer(required=True)
    poutcome = fields.String(required=True)


BANK_MARKETING_MODEL_PARAM_SCHEMA = BankMarketingModelParamSchema()



