from datetime import datetime
import json

def handler(event, context):
    current_time = datetime.now()
    req = event["data"]

    body = {}

    body['data'] = str(current_time)
    body['message'] = "Hello {}".format(req["username"])

    return json.dumps(body)
