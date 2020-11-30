import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
    table = dynamodb.Table('users')
    item = {
        'username': event['username'],
        'password': event['password'],
        'address': event['address'],
        'state': event['state'],
        'country': event['country'],
        'email': event['email'],
        'pan': event['pan'],
        'contact': event['contact'],
        'dob': event['dob'],
        'accounttype': event['accounttype'] 
    }

    response = table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps("user added Successfully"),
}