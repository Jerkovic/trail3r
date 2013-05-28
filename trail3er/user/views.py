# -*- coding: utf-8 -*-


from flask import Blueprint, Response
#from flask import current_app as APP
#from flask.ext.login import login_required, current_user

#from .models import User


user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/')
def index():
    return Response('user index')


