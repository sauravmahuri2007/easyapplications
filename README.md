# EasyApplications
A very simple, extendable, pluggable Django app which allows the user to submit the applications
and registered user to approve and reject the applications submitted by various users.

## Installation & Deployment Guide

| Author                                                             | Version        | Last Updated        |
| ------------------------------------------------------------------ |:--------------:| -------------------:|
| [Saurav Kumar](mailto:saur.k10@gmail.com)                          | 1.0.0          | 9th June, 2018      |


### 1. Install global dependencies

     sudo apt-get install virtualenv python-pip git

### 2. Upgrade `pip` and `setuptools` that are bundled with the OS to the latest stable versions.

     sudo -H pip install pip -U

     sudo -H pip install setuptools -U

### 3. Clone the EasyApplications from github to your preferred directory.

    git clone https://github.com/sauravmahuri2007/easyapplications.git

    cd easyapplications

### 4. Create virtualenv and install project dependencies

    virtualenv --python=python3 venv

    source venv/bin/activate

    pip install -r requirements.txt

### 5. Setup database and tables using migrations and create superuser

    python manage.py migrate

    python manage.py createsuperuser

### 6. Run the app using the default lightweight Django web server (until this app is not part of a big application)

    python manage.py runserver


The app should have started running at http://127.0.0.1:8000

### Note:

1. This is a very simple app and does't require any 3rd-party python packages and only depends on Django.

### ToDo:
1. Automate the installation steps.
2. Deploy the app using a full fledged web server like nginx.
3. Run multiple instances of the app using gunicorn or uwsgi.
4. Create a executable run.py file which will all the server to run without login to virtualenv


