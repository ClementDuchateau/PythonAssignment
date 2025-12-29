# PythonAssignment

My python Assignment is a simple movie tracker.

It allows you to:

Add, edit and list movies

Add and list genres

Export movies to CSV or Excel

Store data in a local SQLite database



Setup instructions

1. clone the repository

git clone https://github.com/ClementDuchateau/PythonAssignment.git



2\. set up a virtual environment

python -m venv venv

venv\\scripts\\activate



3\. install dependancies

pip install -r requirements.txt



4\. create your settings file

copy example\_settings.ini settings.ini



5\. initialize the database and run the program

python -m app.main



Database

the database file is defined in settings.ini

