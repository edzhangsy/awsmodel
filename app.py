import sys
import json
import base64
from detect_simple import image_to_box, main
import time
'''
body: {
    "file_hash": "md5",
    "file_b64": "b64",
    "frame_num": number
}
'''
def handler(event, context):
    body = event["body"]
    try:
        body = json.loads(body)
        file_hash = body['file_hash']
        file_b64 = body['file_b64']
        frame_num = body['frame_num']
        start = time.perf_counter()
        det = image_to_box(file_b64)
        end = time.perf_counter()
        time_elipesd = end - start
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
            'box_string': det,
            'model_time': time_elipesd
        }
        
    }