# openmosqueproject.com

## Install

##### Download procedure
1. Download the project `git clone https://github.com/OpenMosqueProject/openmosqueproject.com`
2. Change branch to django using `git checkout django` 

##### Install procedure
1. Download poetry virtualenv manager, `pip install poetry` - We will use poetry for everything it's simple and easy to use.
2. Type in `poetry install` - make sure that you are on django branch

##### Running APP and migrations
1. We will **always use** `poetry shell` to go into the shell, meaning virtualenv _(venv)_
2. To apply migrations to our database we use classic `python manage.py migrate`
3. To run webapp server we use `python manage.py runserver`
4. Any additional commands we will run inside the virtualenv. This will ensure that we have dependencies installed and a venv. 

----
