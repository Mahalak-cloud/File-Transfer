from google.cloud import storage
import logging
import os

def upload_to_gcs(file_path, bucket_name, gcs_key):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_key)
    try:
        blob.upload_from_filename(file_path)
        logging.info(f"Successfully uploaded {file_path} to GCS bucket {bucket_name} with key {gcs_key}.")
    except Exception as e:
        logging.error(f"Failed to upload {file_path} to GCS bucket {bucket_name} with key {gcs_key}: {e}")
