# -*- coding: utf-8 -*-

"""
General Utilities and Functions
"""

import datetime
import hashlib
import random

from applications.models import Applications

def generate_applicationid():
    """
    generates a unique 16-alnum-char application id.
    """
    hsh = hashlib.sha1(str(datetime.datetime.now()).encode('utf-8')).hexdigest()  # 40 char long hash
    rand = random.randrange(0, 20)
    hsh16 = hsh[rand:rand + 16]
    return hsh16.upper()


def create_application(app_data):
    data = {
        'applicationid': app_data.get('applicationid'),
        'first_name': app_data.get('first_name'),
        'last_name': app_data.get('last_name'),
        'email': app_data.get('email'),
        'status': 'NEWAPPLICATION',
        'updated_dtm': datetime.datetime.now(),
    }
    app = Applications.objects.create(**app_data)
    app.status = 'NEWAPPLICATION'
    app.save()


def get_all_applications(order_by=None):
    try:
        all_apps = Applications.objects.all()
        if order_by:
            all_apps = all_apps.order_by(order_by)
        return all_apps
    except:
        return []


class AppDetails(object):
    """
    Generic application object to get/update application details
    """

    def __init__(self, applicationid):
        self.applicationid = applicationid
        self.application = Applications.objects.get(applicationid=applicationid)

    def get_status(self):
        return self.application.status

    def set_status(self, status):
        self.application.status = status
        self.application.updated_dtm = datetime.datetime.now()
        self.application.save()
        return True

    def __repr__(self):
        return '<Application ({0}: {1} {2} | {3} | {4})>'.format(
            self.applicationid, self.application.first_name, self.application.last_name, self.application.email,
            self.application.status
        )