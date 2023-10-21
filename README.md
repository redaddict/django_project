# django_project on add csv file and import and export
In this project we work on csv file import  and export using django.
csv file is nifty trading data, use csv file fetch data on html page and show niftys candles. 
firstly import csv file on django admin and and html file create fields and show the data. for the csv import and export - 

** install the - pip install django-import-export
and import_export add in settings.py - installed app. 





** admin/ page you can see data in csv file , there you can import or export in json, xml and multiple choice.


** csv data can fetch html page .

** admin page login
username - admin , password- admin123


# first of all you need to set env 
pip list
pip install env
pip install django
py -m venv foldername
//activate the virtual env
foldername\Scripts\activate.bat
// startproject
django-admin startproject TradingProject
cd TradingProject
// startapp
django-admin startapp main app
//check server
py manage.py runserver
//open in vscode
code .



# for django admin page you need -
//py manage.py makemigrations
//py manage.py migrate
# createsuperuser
py manage.py createsuperuser
