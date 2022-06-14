#!/bin/bash
sudo docker build -t awsmodel .
# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
# aws ecr create-repository --repository-name awsmodel --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
sudo docker tag  awsmodel:latest 772639918187.dkr.ecr.us-east-1.amazonaws.com/awsmodel:latest
sudo docker push 772639918187.dkr.ecr.us-east-1.amazonaws.com/awsmodel:latest