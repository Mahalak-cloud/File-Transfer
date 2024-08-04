import os
import sys
import logging
from FileTransfer.s3_uploader import upload_to_s3
from FileTransfer.gcs_uploader import upload_to_gcs
from FileTransfer.config import FILE_TYPES, AWS_S3_BUCKET, GCS_BUCKET

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("file_transfer.log")
        ]
    )

def process_files(directory):
    if not os.path.isdir(directory):
        logging.error(f"The directory {directory} does not exist.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, file_extension = os.path.splitext(file)

            if file_extension[1:] in FILE_TYPES['images'] + FILE_TYPES['media']:
                logging.info(f"Uploading {file_path} to AWS S3 bucket {AWS_S3_BUCKET}.")
                upload_to_s3(file_path, AWS_S3_BUCKET)
            elif file_extension[1:] in FILE_TYPES['documents']:
                logging.info(f"Uploading {file_path} to Google Cloud Storage bucket {GCS_BUCKET}.")
                upload_to_gcs(file_path, GCS_BUCKET)
            else:
                logging.warning(f"Unsupported file type: {file}")

def transfer_files():
    if len(sys.argv) != 2:
        logging.error("Usage: file_transfer <directory-path>")
        sys.exit(1)

    directory = sys.argv[1]
    logging.info(f"Starting file transfer process for directory: {directory}")
    process_files(directory)
    logging.info("File transfer process completed.")

if __name__ == "__main__":
    setup_logging()
    transfer_files()
