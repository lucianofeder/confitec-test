#!/bin/bash

gunicorn -c "gunicorn.conf.py" "app:create_app()"