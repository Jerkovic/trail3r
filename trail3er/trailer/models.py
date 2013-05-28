# -*- coding: utf-8 -*-


#from werkzeug import generate_password_hash, check_password_hash
#from flask.ext.login import UserMixin

from ..extensions import db
#from flask.ext.sqlalchemy import *
#from sqlalchemy.sql import func
#from sqlalchemy.exc import *
from flask.ext.sqlalchemy import *

from slugify import slugify


#from ..utils import get_current_time, SEX_TYPE, STRING_LEN
#from .constants import USER, USER_ROLE, ADMIN, INACTIVE, USER_STATUS


class Trailer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    
    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.slug = slugify(movie_title)

    @property        
    def box_image(self):
        return '%s_%d.jpg' % (self.slug, self.id)
        
    def __repr__(self):
        return '<Trailer %r>' % self.movie_title
    
    @classmethod
    def get_or_404(cls, trailer_id):
        return Trailer.query.get_or_404(trailer_id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def limited(self, limit_count):
        return Trailer.query.order_by('movie_title desc').limit(limit_count).all()


