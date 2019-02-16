# newsfeed
newsfeed project for ReachLocal technical test

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
now the server should be running at http://localhost:8000 .\
You can see the 20 latests articles at http://localhost:8000/news/articles \
or you can get the 100 latests articles by sending a GET request at http://localhost:8000/news/api/articles

I didn't apply PEP8 checks on automatically generated files
