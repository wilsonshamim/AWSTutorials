import boto3

connection = boto3.client(
    'emr',
    aws_access_key_id="ASIAWAQG777R7GVHCPFI",
    aws_secret_access_key = "******",
    aws_session_token = "*******"

)
lst = connection.list_clusters(ClusterStates=['TERMINATED'])

print(lst)
