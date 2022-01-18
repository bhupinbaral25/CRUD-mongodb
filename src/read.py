import json
import math
from src.helpers import response
from model import TODO

from .helpers import skiplimit

def read_todo(event, context):
    response_body = {}
    try:
        parameters = event["queryStringParameters"]
        if(parameters is not None):
            page_size = int(parameters.pop("page_size", 10))
            page_num = int(parameters.pop("page_num", 1))
        else:
            page_size = 10
            page_num = 1

        offset, limit = skiplimit(page_size, page_num)

        todo = TODO.objects.skip(offset).limit(limit)
        todo_count = todo.count()
        response_body = {
            "data": json.loads(todo.to_json()),
            "msg": "TODO query successfully",
            "total_page_num": math.ceil(todo_count / page_size),
            "status": True
        }
        status_code = 200
    except Exception as e:
        response_body = {
            "status": False,
            "msg": str(e)
        }
        status_code = 400
    return response(status_code, response_body)
