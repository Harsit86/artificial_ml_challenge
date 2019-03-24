import io
import csv
from sqlalchemy.exc import DatabaseError
from flask import (
    Blueprint,
    request,
    jsonify,
)

from app.models import CustomerDetails
from app.db import db
from logger import get_logger


log = get_logger(__name__)
file_upload_bp = Blueprint('file_upload', __name__, url_prefix='/upload')



@file_upload_bp.route('/csv', methods=['POST'])
def upload_csv():
    file = request.files.get('file', None)
    if not file :
        return jsonify('Error: no file found in request payload, expected a csv file.'), 400

    try:
        num_rows = 0
        for row in csv.DictReader(io.StringIO(file.stream.read().decode('utf-8')), delimiter=';'):
            cd = CustomerDetails(**row)
            db.session.add(cd)
            num_rows += 1
        db.session.commit()
        log.info(f'Uploaded {num_rows} rows to DB.')
        return jsonify({'status': f'Success. Uploaded {num_rows} rows.'}), 200

    except DatabaseError as e:
        db.session.rollback()
        log.info(f'Faile to uploaded data, error: {str(e)}.')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
