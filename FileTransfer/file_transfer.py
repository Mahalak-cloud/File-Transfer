import os
import sys
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from FileTransfer.s3_uploader import upload_to_s3
from FileTransfer.gcs_uploader import upload_to_gcs
from FileTransfer.config import FILE_TYPES, AWS_S3_BUCKET, GCS_BUCKET

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("file_transfer_logs.log")
        ]
    )

def sanitize_path(file_path, root_directory):
    relative_path = os.path.relpath(file_path, root_directory)
    return relative_path.replace("\\", "/")

def upload_file(file_path, root_directory):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension[1:].lower()
    sanitized_path = sanitize_path(file_path, root_directory)

    if file_extension in FILE_TYPES['images'] + FILE_TYPES['media']:
        logging.info(f"Uploading {file_path} to AWS S3 bucket {AWS_S3_BUCKET}.")
        upload_to_s3(file_path, AWS_S3_BUCKET, sanitized_path)
    elif file_extension in FILE_TYPES['documents']:
        logging.info(f"Uploading {file_path} to Google Cloud Storage bucket {GCS_BUCKET}.")
        upload_to_gcs(file_path, GCS_BUCKET, sanitized_path)
    else:
        logging.warning(f"Unsupported file type: {file_path}")


# handling high volume
def process_files(directory):
    if not os.path.isdir(directory):
        logging.error(f"The directory {directory} does not exist.")
        return

    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(upload_file, file_path, directory) for file_path in file_paths]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Error occurred: {e}")

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
