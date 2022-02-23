import boto3

connection = boto3.client(
    'emr',
    region_name='us-west-2',
    aws_access_key_id="***",
    aws_secret_access_key="***",
    aws_session_token="****"
)

cluster_id = connection.run_job_flow(
    Name='Wilson_EMR',
    LogUri='s3://bucketname/wilsonshamim/emr/logs',
    ReleaseLabel='emr-6.5.0',
    Applications=[
        {
            'Name': 'Spark'
        },
    ],
    Instances={
        'InstanceGroups': [
            {
                'Name': "Master nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 1,
            },
            {
                'Name': "Slave nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 2,
            }
        ],
        'Ec2KeyName': 'wilsonkeypair',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2SubnetId': 'subnet-02****',
    },
    
    VisibleToAllUsers=True,
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    Tags=[
        {
            'Key': 'name',
            'Value': 'wilsonERM',
        },
        {
            'Key': 'owner',
            'Value': 'wilson',
        },
       
    ],
)

print ('cluster created with the step...', cluster_id['JobFlowId'])
