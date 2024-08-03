from google.cloud import storage
import os

def upload_to_gcs(file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)

    try:
        blob.upload_from_filename(file_path)
        print(f'Successfully uploaded {file_path} to {bucket_name}')
    except FileNotFoundError:
        print(f'The file was not found: {file_path}')
