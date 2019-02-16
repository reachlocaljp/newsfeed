# newsfeed
just a small project using newsapi data for ReachLocal technical test

## Requirements
Python >= 3.6 \
Django >= 2.1.7

## Setup
### Installation
first install python dependencies
```
pip install -r requirements.txt
```
### Populate database
We will use sqlite3 (the default one) in this project. So we don't need any special setup, just use
```
python manage.py migrate
```
It will both create the database and apply migrations

then to get data from newsapi, use
```
python manage.py fetch_articles yourapikey
```
I just chose to take top headlines from business in US

### Run server and API
First create a file called secret_key.py and give a value to the secret_key
```
SECRET_KEY = 'putyoursecretkeyhere'
```

then run the server with
```
python manage.py runserver
```
Now the server should be running at http://localhost:8000\
You can see the 20 latests articles at http://localhost:8000/news/articles\
or you can get the 100 latests articles by sending a GET request at http://localhost:8000/news/api/articles\
In that case they will be returned in JSON format.

### Miscellaneous
I didn't apply PEP8 (now pycodestyle) checks on automatically generated files and think they should change the 80 characters limit to 100. \
I am aware that there may be some poor naming choices, but I'm doing my best for this. \
I didn't follow the usual git workflow (branch -> pull request -> merge into master) and committed directly into master, I should be sent to Hell for that. \
I didn't write unit tests because I didn't have time to prepare mock data, but that is not something I would tolerate for a professional project.
