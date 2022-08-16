import boto3
from src.config import Config

def load_s3_client():
    boto3_session = boto3.Session(
        profile_name=Config.PROFILE_NAME,
        region_name=Config.REGION_NAME
    )
    s3_client = boto3_session.client(service_name='s3')
    return s3_client
