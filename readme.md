# DnD Character Creator in Django
This project is a web app to create DnD characters and access them!

This app is made using Django and was made to use a SQLite database.

To run locally, you'll need to create a virutal environement, install packages, create a superuser, then start the local server.

1. After cloning the project, run `python -m venv .venv`
2. To install packages, first activate you virutal environment, then run `pip install -r requirements.txt`
3. Next you need to create a superuser to access the admin pages, navigate to /DnDCharacter/, then run `python manage.py createsuperuser`. Note the account information you enter.
4. Now you can start the server by running `python manage.py runserver`!