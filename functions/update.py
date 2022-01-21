import json
from model import TODO
from functions.helpers.response import response

def main(event, context):
    
    try:
        data = json.loads(event["body"])
        todo_id = data.pop("id", None)
        if todo_id is not None:
            NOT_REQUIRED = ["id", "creation_date", "_cls"]
            schema_fields = [key for key, value in TODO._fields.items() if key not in NOT_REQUIRED]
            print(schema_fields)
            print(data)
            # * key value pairs of updated attributes
            data_update = {item: data[item] for item in data if item in schema_fields and data[item] is not None}
            print(data_update)


            # * Update given parameters in respective Collection
            # TODO.objects(id=todo_id).update(**data_update)
            todo = TODO.objects(id=todo_id)
            todo.update(**data_update)
            body = {
                "status": True,
                "msg": "todo updated successfully",
                "data": json.loads(todo.to_json())
                
            }
        else:
            body = {
                "status": True,
                "msg": "todo Id should pass for update operation"
            }
        status_code = 200
    except Exception as e:
        body = {
            "status": False,
            "msg": str(e)
            }
        status_code = 400
    return response(status_code, body)
