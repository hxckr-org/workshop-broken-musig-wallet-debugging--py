#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${GREEN}Setting up development environment...${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 is not installed. Please install Python 3 first.${NC}"
    exit 1
fi

echo "Creating virtual environment..."
python3 -m venv .hxckr

echo "Installing dependencies..."
source .hxckr/bin/activate

if [[ "$VIRTUAL_ENV" != *"hxckr"* ]]; then
    echo -e "${RED}Virtual environment activation failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Virtual environment activated! ($(which python))${NC}"

pip install -r requirements.txt

echo "Run \`source .hxckr/bin/activate\` to activate the virtual environment"

chmod +x your_program.sh

echo -e "${GREEN}Setup complete and virtual environment activated!${NC}"
echo -e "${BLUE}You can now run:${NC} ${GREEN}./your_program.sh${NC}"
echo -e "When you're done, type: ${GREEN}deactivate${NC}"
echo -e "\n${BLUE}Current Python path:${NC} ${GREEN}$(which python)${NC}"
echo -e "${BLUE}Virtual env location:${NC} ${GREEN}$VIRTUAL_ENV${NC}"


exec $SHELL 