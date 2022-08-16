from flask import Blueprint, request
import requests
from src.config import Config
from src.helper.common import load_s3_client

pre_signed_url = Blueprint(
    name='pre_signed_url',
    import_name=__name__
)

@pre_signed_url.route('/upload_pre_signed_url_file', methods=['POST'])
def upload_pre_signed_url_file():
    s3_client = load_s3_client()
    
    body_form_data = request.files
    file_name = body_form_data.get('target_file').filename
    file_data = body_form_data.get('target_file')

    presigned_post = s3_client.generate_presigned_post(
        Bucket=Config.S3_BUCKET,
        Key=file_name,
        Fields=None,
        Conditions=None,
        ExpiresIn=3600
    )

    with requests.Session() as req_session:
        req_session.post(
            url=presigned_post.get('url'),
            data={
                'key': presigned_post.get('fields').get('key'),
                'policy': presigned_post.get('fields').get('policy'),
                'x-amz-algorithm': presigned_post.get('fields').get('x-amz-algorithm'),
                'x-amz-credential': presigned_post.get('fields').get('x-amz-credential'),
                'x-amz-date': presigned_post.get('fields').get('x-amz-date'),
                'x-amz-signature': presigned_post.get('fields').get('x-amz-signature'),
            },
            files={
                'file': file_data.read()
            }
        )

    return 'upload complete'
