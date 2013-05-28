# -*- coding: utf-8 -*-


from flask import Blueprint, Response, render_template
#from ..utils import get_current_time
from .models import Trailer


trailer = Blueprint('trailer', __name__, url_prefix='/trailer')

@trailer.route('/')
def index():
    trailers = Trailer.limited(50)
    return render_template("trailer/index.html", trailers=trailers)
