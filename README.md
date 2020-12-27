# python-for-web-Fedy
teaching Fedy python and Django
# 1. Django
this explains how to use [Django](https://www.djangoproject.com/)
## 1.1. Install
- Open cmd or termial and type
``` 
pip install Django 
```
- Navigate to folder you want to generate your project an use the `django-admin cli`
``` 
django-admin startproject YOUR_PROJECT_NAME
```
Navigate into the folder holding your project name and use the following command
- Check the changes to the models
``` 
python manage.py makemigrations
```
- Apply changes to the database
``` 
python manage.py migrate
```
- Create Super User
``` 
python manage.py createsuperuser
```
- run the server
``` 
python manage.py runserver
```