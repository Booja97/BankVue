import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    table = dynamodb.Table('users')
    response = table.update_item( Key={"username": event["username"]} ,ExpressionAttributeNames={  '#state': 'state' },
                        ExpressionAttributeValues={
                        ':password': event['password'],':accounttype': event['accounttype'],
                        ':address': event['address'],':state': event['state'],':country': event['country'],':email': event['email'],
                        ':pan': event['pan'],':contact': event['contact'],':dob': event['dob']},
                        UpdateExpression='SET  password = :password, address = :address, #state = :state, country = :country, email = :email, pan = :pan, contact = :contact, accounttype = :accounttype, dob= :dob')
    return {
        'statusCode': 200,
        'body': json.dumps("account updated successfully")
    }