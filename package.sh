#!bin/sh
RED='\033[1;31m'
NC='\033[0m' # No Color

echo "${RED}Create a ZIP archive of the library.${NC}"
cd package && zip -r9 ${OLDPWD}/function.zip .
echo " "

echo "${RED}Add function code to the archive.${NC}"
cd $OLDPWD && zip -g function.zip function.py server_list.json