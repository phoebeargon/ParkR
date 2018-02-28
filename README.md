# ParkR
Senior project for CS 425

Uses Django 2.0 and Python 3


Usage
------

Create the directory where you would like to store the project

Clone the project into this new directory
```
    $ git clone https://github.com/phoebeargon/ParkR.git
```

Create and activate a virtual environment to work in within your new directory (must be named env):
```
    $ python3 -m venv env
    $ . env/bin/activate
```

Install requirements for the project on your virtual environment:
```
    (env) $ pip install django django-crispy-forms
```


To run the project locally:

In the main project folder (same folder with manage.py) run:
```
    $ python manage.py runserver
```

Now if you open `localhost:8000` in the browser you should see the website


You can make and test changes locally. When you are happy with all of your changes, push to the project github.

The server will automatically pull down any changes from the github, so you can now see your changes live at phoebeargon.com