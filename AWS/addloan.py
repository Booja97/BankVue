import json
import os
import boto3
import decimal
import uuid

dynamodb = boto3.resource("dynamodb")

class DecimalEncode(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncode, self).default(o)

def lambda_handler(event, context):
    table = dynamodb.Table('UserLoan')
    item = {
        'id': str(uuid.uuid1()),
        'username': event['username'],
        'loan_type': event['loan_type'],
        'loan_Amount': event['loan_Amount'],
        'date': event['date'],
        'rate_of_interest': event['rate_of_interest'],
        'duration_of_loan': event['duration_of_loan']
    }
    print(item)
    response = table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps("Loan added Successfully"),
        'headers': {'Content-Type': 'application/json'}
}
  