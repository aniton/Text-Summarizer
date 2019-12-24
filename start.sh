#!/bin/bash
echo $(pwd)
export PYTHONPATH=./
export FLASK_APP=./app/app_1.py
echo $FLASK_APP
flask run --port 5000 &
#python ./app/app_1.py
export FLASK_APP=./app/app_2.py
flask run --port 5001
#python ./app/app_2.py

