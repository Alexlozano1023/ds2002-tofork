import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-alexlozano'
file_key = 'google_logo.png'

url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': file_key},
    ExpiresIn=60  # 60 seconds
)

print("Presigned URL:", url)

