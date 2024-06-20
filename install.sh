#!/usr/bin/bash

git clone https://github.com/crimsonslate/ecom.git
cd ecom/
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate
python manage.py runserver
