#!/bin/bash

python -m pip install --upgrade pip

pip install --upgrade pippip install --force-reinstall -U setuptools


pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
 
