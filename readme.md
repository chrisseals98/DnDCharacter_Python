# DnD Character Creator in Django
This project is a web app to create DnD characters and access them!

This app is made using Django and was made to use a SQLite database.

##Running Locally
To run locally, you'll need to create a virtual environment, create a secret key, install packages, create a superuser, and then start the local server.

1. After cloning the project, run `python -m venv .venv`
2. To create the secret key, simply create a text file in your virtual environment directory called secret_key.txt. File path will be `.venv/secret_key.txt`. Then put in a secret to be used.
3. To install packages, first activate your virtual environment, then run `pip install -r requirements.txt`
4. Next you need to create a superuser to access the admin pages, navigate to `/DnDCharacter/`, then run `python manage.py createsuperuser`. Please be sure to note the account information you enter.
5. Now you can start the server by running `python manage.py runserver`!
