import json
from src.helpers import response
from model import TODO


def delete_todo(event, context):
    response_body = {}
    try:
        data = json.loads(event["body"])
        todo_id = data.pop("id", None)
        if todo_id is not None:
            TODO.objects.get(id=todo_id).delete()
            response_body = {
                "status": True,
                "msg": "todo deleted successfully"
            }
        else:
            response_body = {
                "status": False,
                "msg": "todo Id should pass for deletion operation"
            }
        status_code = 200
    except Exception as e:
        response_body = {
            "status": False,
            "msg": str(e)
        }
        status_code = 400
    return response(status_code, response_body)
