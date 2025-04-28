import boto3
import requests

bucket = 'ds2002-alexlozano'  # Replace with your bucket if needed
url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
filename = 'from_web.png'

# Download file
response = requests.get(url)
with open(filename, 'wb') as f:
    f.write(response.content)

# Upload to S3
s3 = boto3.client('s3', region_name='us-east-1')
s3.upload_file(filename, bucket, filename)

# Generate presigned URL
presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': filename},
    ExpiresIn=300  # 5 minutes
)

print("Presigned URL:", presigned_url)

