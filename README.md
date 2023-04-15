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

Your output should look something like:

![image](https://user-images.githubusercontent.com/411454/232252309-a825adc8-a3af-4ce7-985b-9d8049063ac0.png)
