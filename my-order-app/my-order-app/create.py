import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')

def lambda_handler(event, context):
    
    orders = json.loads(event['body'])
    table = dynamodb.Table(table_name)
    
    for each_order in orders:
        table.put_item(Item=each_order)
        
    return{
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'message': 'Order Created'})
    }