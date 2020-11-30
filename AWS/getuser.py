import json
import os
import boto3
import decimal
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource("dynamodb")

class DecimalEncode(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncode, self).default(o)

def lambda_handler(event, context):
    # TODO implement
    table = dynamodb.Table('users')
    response = table.scan(FilterExpression=Attr('username').eq(event['username']) )
    return {
        'statusCode': 200,
        'body': json.dumps(response, cls=DecimalEncode),
        'headers': {'Content-Type': 'application/json'}
}

Integration Request:
When there are no templates defined 
application/json
{
  "username": "$input.params('username')"
}
