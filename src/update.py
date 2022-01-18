import json
from flask import response, jsonify
from model import TODO


def update_todo(event, context):
    response_body = {}
    try:
        data = json.loads(event["body"])
        todo_id = data.pop("id", None)
        if todo_id is not None:
            NOT_REQUIRED = ["id", "creation_date", "_cls"]
            schema_fields = [key for key, value in TODO._fields.items() if key not in NOT_REQUIRED]
            # * key value pairs of updated attributes
            data_update = {item: data[item] for item in data if item in schema_fields and data[item] is not None}

            # * Update given parameters in respective Collection
            todo = TODO.objects.get(id=todo_id)
            todo.update(**data_update)
            todo.reload()
        
            response_body = {
                "status": True,
                "msg": "todo updated successfully"
            }
        else:
            response_body = {
                "status": False,
                "msg": "todo Id should pass for update operation"
            }
        status_code = 200
    except Exception as e:
        response_body = {
            "status": False,
            "msg": str(e)
            }
        status_code = 400
    return response(status_code, jsonify(response_body))
