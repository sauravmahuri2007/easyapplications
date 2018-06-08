# -*- coding: utf-8 -*-

"""
General Utilities and Functions
"""

import datetime
import hashlib
import random

def generate_applicationid():
    """
    generates a unique 16-alnum-char application id.
    """
    hsh = hashlib.sha1(str(datetime.datetime.now()).encode('utf-8')).hexdigest()  # 40 char long hash
    rand = random.randrange(0, 20)
    hsh16 = hsh[rand:rand + 16]
    return hsh16.upper()