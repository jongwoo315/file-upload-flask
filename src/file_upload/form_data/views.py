from flask import Blueprint, request
from src.config import Config
from src.helper.common import load_s3_client

form_data = Blueprint(
    name='form_data',
    import_name=__name__
)

@form_data.route('/upload_form_data_file', methods=['POST'])
def upload_form_data_file():
    s3_client = load_s3_client()

    body_form_data = request.files

    s3_response = s3_client.put_object(
        Bucket=Config.S3_BUCKET,
        Key=body_form_data.get('target_file').filename,
        Body=body_form_data.get('target_file')
    )

    return s3_response
