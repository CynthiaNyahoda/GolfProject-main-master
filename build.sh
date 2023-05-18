#!/bin/bash

pip install --upgrade pippip install --force-reinstall -U setuptools
python manage.py makemigrations
python manage.py migrate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
