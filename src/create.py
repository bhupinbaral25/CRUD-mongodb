import json
from src.helpers import response
from model import TODO

def create_todo(event, context):
    response_body = {}
    try:
        data = json.loads(event["body"])
        todo = TODO(**data).save()
        response_body = {
            "data": json.loads(todo.to_json()),
            "status": True,
            "msg": "todo created successfully"
        }
        status_code = 200
    except Exception as e:
        response_body = {
            "msg": str(e), 
            "status": False
        }
        status_code = 400
    return response(status_code, response_body)
