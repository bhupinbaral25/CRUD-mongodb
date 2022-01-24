import json
from functions.helpers.response import response
from model import TODO
from functions.helpers.validation import ValidateDeleteModel


def main(event, context):
    try:
        data = json.loads(event["body"])
        ValidateDeleteModel(**data)
        status_code = 200  
        todo_id = data.pop("id", None)
        if todo_id is not None:
            TODO.objects.get(id=todo_id).delete()
            body = {
                "status": True,
                "msg": "todo deleted successfully"
            }
        else:
            body = {
                "status": True,
                "msg": "todo Id should pass for deletion operation"
            }   
             
    except Exception as e:
        status_code = 400
        body = {
            "status": False,
            "msg": str(e)
        }

    return response(status_code, body)
