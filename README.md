**File Transfer Module**

The File Transfer Module is a Python package designed to efficiently manage and automate the transfer of various file types from a specified directory (and its subdirectories) to cloud storage services. The module categorizes and uploads image and media files to Amazon Web Services (AWS) S3, and document files to Google Cloud Storage (GCS). This is especially useful for applications dealing with a large number of files, ensuring efficient, scalable, and automated file management.

**Set Up Your Environment**
Clone the Repository:

git clone <repository-url>
cd <repository-name>

**Create and Activate a Virtual Environment**

python -m venv virtual_env
virtual_env\Scripts\activate

**Install Dependencies**

pip install -r requirements.txt

**Configure AWS and Google Cloud Credentials**
AWS Credentials:

Ensure you have your AWS credentials configured. You can use the AWS CLI to configure them:

aws configure

export AWS_ACCESS_KEY_ID='your-access-key-id'
export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
export AWS_DEFAULT_REGION='your-region'


**Configure Google Cloud Credentials**

Ensure you have your Google Cloud credentials JSON file. Set the environment variable to point to this file:
export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/credentials-file.json'


**Configure the Project**
Update Configuration:

Open FileTransfer/config.py and update the bucket names and file types if necessary.
FILE_TYPES = {
    'images': ['jpg', 'png', 'svg', 'webp'],
    'media': ['mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm'],
    'documents': ['doc', 'docx', 'csv', 'pdf']
}

AWS_S3_BUCKET = 'your-s3-bucket-name'
GCS_BUCKET = 'your-gcs-bucket-name'


**Run the script with the directory containing your files**

Terminal: 
python -m FileTransfer.file_transfer /path/to/your/files

Example:  python -m FileTransfer.file_transfer C:\Users\Maha\AWS_Test

---------------------------------------------------------------------------------------------------------------------------------------
