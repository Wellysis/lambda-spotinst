#!bin/sh
RED='\033[1;31m'
NC='\033[0m' # No Color

echo "${RED}Deploy lambda.${NC}"
aws lambda create-function --function-name spot-inst --zip-file fileb://function.zip --handler function.spotinst-handler --runtime python3.7 --role arn:aws:iam::937127283640:role/lambda-cli-role