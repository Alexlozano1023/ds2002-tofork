import boto3

s3 = boto3.client('s3', region_name='us-east-1')
response = s3.list_buckets()

for r in response['Buckets']:
    print(r['Name'])

