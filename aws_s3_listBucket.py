import boto3
print('This code is to get the list of AWS S3 buckets')
aws_access_key_id = "***"
aws_secret_access_key = "***"
aws_session_token = "***"
s3_client = boto3.client('s3',aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token)
response = s3_client.list_buckets()
print(response)
