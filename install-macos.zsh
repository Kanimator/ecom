#!/bin/zsh

cd $HOME
brew install python pyenv node
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm install -D package.json
