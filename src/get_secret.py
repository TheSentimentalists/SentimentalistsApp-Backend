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

    error_messages = {
        'AccessDeniedException' : 'Key Access Failure',
        'DecryptionFailureException' : 'Key Decryption Failure',
        'InternalServiceErrorException' : 'Server Side Error',
        'InvalidParameterException' : 'Invalid Parameter',
        'InvalidRequestException' : 'Invalid Request',
        'ResourceNotFoundException' : 'Resource Not Found',
        'Generic' : 'Unspecified Error Occured'
    }

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
        error = error_messages['Generic']
        if 'Error' in e.response:
            aws_error_code = e.response['Error'].get('Code', 'Generic')
            error = error_messages.get(aws_error_code, error_messages['Generic'])
        return {'error': error}
    else:
        return json.loads(get_secret_value_response['SecretString'])
