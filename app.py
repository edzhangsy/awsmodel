import sys
import json
import base64
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
        frame_num = body['frame_num']
        out_box_json = image_to_box(file_b64)
    except AssertionError:
        return {
            'statusCode': 500,
            'message': "assertion error"
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 500,
            'message': "json decode error"
        }
    except Exception:
        return {
            'statusCode': 500,
            'message': "execuate logic error"
        }

    # TODO check file hash
    return {
        'statusCode': 200,
        'body': {
            'frame_num': frame_num,
            'file_hash': file_hash,
            'box_string': out_box_json
        }
        
    }
