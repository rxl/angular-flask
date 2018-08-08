# AngularJS + Flask Boilerplate App

A template for building apps with an Angular frontend and a Flask / python backend.

### How to Get Started

1. clone this repo

2. install all the necessary packages (best done inside of a virtual environment)

  > sudo apt install python3-pip

  > pip3 install -r requirements.txt

3. run the app
> python3 runserver.py

4. create and seed the db (the server must still be running, so open a new terminal window first)
> python3 manage.py create_db && python3 manage.py seed_db --seedfile 'data/db_items.json'

5. check out your blog
> http://localhost:5000/blog

6. if you like this project, give it a star :)
