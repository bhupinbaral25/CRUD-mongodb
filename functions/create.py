import json
import os
from functions.helpers.response import response
from model import TODO

def main(event, context):
    
    try:
        data = json.loads(event["body"])
        print(data)
        todo = TODO(**data).save()
        status_code = 200
        body = {
        "datas": json.loads(todo.to_json()),
        "msg": "todo created successfully",
        "status": True,
        }    

    except Exception as e:
        status_code = 400
        body = {
            "msg": str(e), 
            "status": True,
        }
    
    return response(status_code, body)
