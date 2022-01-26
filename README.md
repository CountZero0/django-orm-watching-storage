# Bank storage security console
***
## Description

This web application allows you to monitor access to bank storage.You can get information about active passcards, all visits by any user and users in storage at right moment. 

### Getting started

Use pip to install dependencies:
>python -m pip install -r requirements.txt

You need to create .env file with such strings:
>DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
> 
>SECRET_KEY=Secret key value
> 
>DEBUG=Debug mode
> 
>ALLOWED_HOSTS=List of allowed hosts

### To run web service you need to type in terminal:
>python manage.py runserver

### Then just open your browser and type:
>127.0.0.1:8000

##Project goals
The code is written for educational purposes. Training course for web-developers https://dvmn.org/.