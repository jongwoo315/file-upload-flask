from flask import Blueprint, request
from src.config import Config
from src.helper.common import load_s3_client

basic = Blueprint(
    name='basic',
    import_name=__name__
)

@basic.route('/upload_basic_file', methods=['POST'])
def upload_basic_file():
    s3_client = load_s3_client()

    query_string = request.args.to_dict()
    body_binary_data = request.data

    s3_response = s3_client.put_object(
        Bucket=Config.S3_BUCKET,
        Key=query_string['filename'],
        Body=body_binary_data
    )

    return s3_response
