import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-alexlozano'
local_file = 'google_logo.png'

with open(local_file, 'rb') as f:
    s3.put_object(
        Body=f,
        Bucket=bucket,
        Key=local_file
    )

print("File uploaded privately.")

