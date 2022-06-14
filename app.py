import sys
from car_detection import image_to_box
'''
event: {
    "file_hash": "md5",
    "file_b64": "b64"
}
'''
def handler(event, context):
    file_hash = event['file_hash']
    file_b64 = event['file_b64']
    try:
        out_box_json = image_to_box(file_b64)
    except Exception:
        return {
            'statusCode': 500
        }

    # TODO check file hash
    return {
        'statusCode': 200,
        'body': {
            'file_hash': file_hash,
            'box_string': out_box_json
        }
        
    }