#This is the settings.py file

from os import environ
#SECRET_KEY=environ.get('SECRET_KEY')
API_KEY=environ.get('API_KEY')
#MYSQL_USER=environ.get('MYSQL_USER')
SQLALCHEMY_DATABASE_URI=environ.get('SQLALCHEMY_DATABASE_URI')

# add any more variables you have