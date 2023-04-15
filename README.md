# Instructions
Create a virtual env:
`python -m venv ~/.virtualenvs/query-example`

Install deps:
`pip install -r requirements.txt`

Make migrations:
`python manage.py makemigrations`

Run migrations:
`python manage.py migrate`

Seed Database:
`python manage.py seed`

Finally - display query output:
`python manage.py show_query`