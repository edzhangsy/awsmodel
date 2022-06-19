import sys
import json
from car_detection import image_to_box
'''
body: {
    "file_hash": "md5",
    "file_b64": "b64"
}
'''
def handler(event, context):
    body = event["body"]
    try:
        body = json.loads(body)
        file_hash = body['file_hash']
        file_b64 = body['file_b64']
        out_box_json = image_to_box(file_b64)
    except Exception:
        return {
            'statusCode': 500,
            'message': "json or b64 error"
        }

    # TODO check file hash
    return {
        'statusCode': 200,
        'body': {
            'file_hash': file_hash,
            'box_string': out_box_json
        }
        
    }
