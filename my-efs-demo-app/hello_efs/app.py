import simplejson as json
from pathlib import Path

FILE = Path("/mnt/lambda/file")

def lambda_handler(event, context):
    
    method_type = event["httpMethod"]
    
    if method_type == "GET":    
        wrote_file = False
        contents = None
        if not FILE.is_file():
            with open(FILE, 'w') as f:
                contents = "Hello, EFS, I was just born!\n"
                f.write(contents)
                wrote_file = True
        else:
            with open(FILE, 'r') as f:
                contents = f.read()
        return {
            "statusCode": 200,
            "body": json.dumps({
                "file_contents": contents,
                "created_file": wrote_file
            }),
        }
    
    elif method_type == "POST":
        
        new_data = event["body"]

        with open(FILE, 'w') as f:
            f.write(new_data)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "file_contents": "updated"
            }),
        }
