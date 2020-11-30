import json
import os
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
 
    table = dynamodb.Table('users')
    response = table.scan(FilterExpression=Attr('username').eq(event['username']) & Attr('password').eq(event['password'])  )
    print(response['Count'])
    if response['Count'] == 0:
        return {
            'statusCode': 400,
            'body': json.dumps("Username or password is incorrect")
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps("Login successful")
        }
