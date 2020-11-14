from aws_xray_sdk.core import xray_recorder
import boto3
import base64
import json
from botocore.exceptions import ClientError


@xray_recorder.capture('getSecret')
def get_secret(secret_name, region_name):
    """
    Output: Dict (Secret Key/Value Pairs)
    This function calls a stored secret from AWS Secret Manager.
    It returns the requested secret as a dict of key/value pairs.
    Otherwise, it will return an 'error'.
    """

    """
    Create a Secrets Manager client
    """
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    """
    Try obtain the secret, handle a few exceptions
    """
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDeniedException':
            """
            Function doesn't have the right permissions.
            """
            return {'error': 'Key Access Failure'}
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            """
            Secrets Manager can't decrypt the protected secret text using the
            provided KMS key.
            """
            return {'error': 'Key Decryption Failure'}
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            """
            An error occurred on the server side.
            """
            return {'error': 'Server Side Error'}
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            """
            You provided an invalid value for a parameter.
            """
            return {'error': 'Invalid Parameter'}
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            """
            You provided a parameter value that is not valid for the current
            state of the resource.
            """
            return {'error': 'Invalid Request'}
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            """
            We can't find the resource that you asked for.
            """
            return {'error': 'Resource Not Found'}
    else:
        return json.loads(get_secret_value_response['SecretString'])
