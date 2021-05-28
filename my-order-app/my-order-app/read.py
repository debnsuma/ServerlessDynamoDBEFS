import simplejson as json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
  
    if event["queryStringParameters"]:
        order_id = int(event["queryStringParameters"]["id"])
        orders = table.query(KeyConditionExpression=Key("id").eq(order_id))
    else:
        orders = table.scan()
        
    return {
            'statusCode' : 200,
            'headers' : {},
            'body' : json.dumps(orders['Items'])
            }   