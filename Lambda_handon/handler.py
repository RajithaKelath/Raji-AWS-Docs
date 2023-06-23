import json
import time

def hello(event, context):  #"context" is not accessed
    """
    body = {
        "message": "Go serverless!",
        "input" : event
    }

    response = {
        "StatusCode": 200,
        "body" : json.dumps(body)
    }

    return response
    """
    print ("Hello World!")
    time.sleep(4)
    return "Another hello world"
