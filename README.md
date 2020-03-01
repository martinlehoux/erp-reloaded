# erp-reloaded
![CI](https://github.com/martinlehoux/erp-reloaded/workflows/CI/badge.svg)
A full Django 3.0 ERP software

## Development
* `python manage.py migrate` Create the database schemas
* `python manage.py loaddata fixtures/*.json` Load initial data
* `docker run -p 6379:6379 -d redis` Start redis containier for cache
* `python manage.py runserver` Run a development server