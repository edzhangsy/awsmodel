# modeling

this branch is for aws lambda function deployment

first, install docker and awscli

second, put pretrained model `yolo.h5` in model_data directory

follow [docker in aws](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-from-base) to generate docker file and upload to aws lambda

to test main functionality

1. dependency installation `pip install -r requirement.txt`

2. usage `python car_detection.py pictures/1.jpg`
