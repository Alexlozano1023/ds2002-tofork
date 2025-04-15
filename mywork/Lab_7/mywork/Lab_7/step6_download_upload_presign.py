import boto3
import requests

bucket = 'ds2002-alexlozano'
image_url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
filename = 'downloaded_image.png'

# Download image
img = requests.get(image_url)
with open(filename, 'wb') as f:
    f.write(img.content)

# Upload
s3 = boto3.client('s3', region_name='us-east-1')
s3.upload_file(filename, bucket, filename)

# Presign
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': filename},
    ExpiresIn=300
)

print("Presigned URL:", url)

