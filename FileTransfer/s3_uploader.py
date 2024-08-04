import boto3
import logging
from boto3.s3.transfer import TransferConfig

def upload_to_s3(file_path, bucket_name, s3_key):
    s3_client = boto3.client('s3')
    config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                            multipart_chunksize=1024 * 25, use_threads=True)
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key, Config=config)
        logging.info(f"Successfully uploaded {file_path} to S3 bucket {bucket_name} with key {s3_key}.")
    except Exception as e:
        logging.error(f"Failed to upload {file_path} to S3 bucket {bucket_name} with key {s3_key}: {e}")
