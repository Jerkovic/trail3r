# -*- coding: utf-8 -*-

import os
 
class BaseConfig(object):

    PROJECT = "Trail3r"
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret_key'
    UPLOAD_FOLDER = upload_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads')

class DefaultConfig(BaseConfig):

    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/trail3r.db'
    

class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/trail3er_test.db'
