#!bin/sh
RED='\033[1;31m'
NC='\033[0m' # No Color

export OLDPWD=$(pwd)
echo "${RED}Check current directory.${NC}"
echo "${OLDPWD}"
echo " "

echo "${RED}Create package folder.${NC}"
mkdir package
echo " "

echo "${RED}Install library...${NC}"
pip install --target ./package requests