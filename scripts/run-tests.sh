# /bin/bash
set -e

python -m flake8
coverage run manage.py test
coverage report
isort --diff --skip migrations
