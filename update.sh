#!bin/sh
RED='\033[1;31m'
NC='\033[0m' # No Color

sh package.sh
echo " "
echo "${RED}Update lambda.${NC}"
aws lambda update-function-code --function-name spot-inst --zip-file fileb://function.zip