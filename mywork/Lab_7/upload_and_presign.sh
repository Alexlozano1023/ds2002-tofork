#!/bin/bash

# Usage: ./upload_and_presign.sh <filename> <bucket-name> <expiration-time>
FILE=$1
BUCKET=$2
EXPIRATION=$3

# Upload file to S3
aws s3 cp "$FILE" s3://$BUCKET/

# Generate a presigned URL
aws s3 presign s3://$BUCKET/$FILE --expires-in $EXPIRATION

