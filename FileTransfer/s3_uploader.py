import boto3
from botocore.exceptions import NoCredentialsError
import os
import logging

def upload_to_s3(file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        logging.info(f"Successfully uploaded {file_path} to S3 bucket {bucket_name}.")
        print(f'Successfully uploaded {file_path} to {bucket_name}')
    except FileNotFoundError as e:
        logging.error(f"Failed to upload {file_path} to S3 bucket {bucket_name}: {e}")
        print(f'The file was not found: {file_path}')
    except NoCredentialsError as e:
        logging.error(f" Credentials unavailable: {e}")
        print('Credentials not available')
