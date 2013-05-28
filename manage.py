# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from trail3er import create_app
from trail3er.extensions import db


from bs4 import BeautifulSoup
import os
import re
import urllib
import urllib2

from trail3er.trailer.models import Trailer

app = create_app(app_name='trail3er')
manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""
    app.run()


@manager.command
def initdb():
    """Init/reset database."""
    db.drop_all()
    db.create_all()


@manager.command
def import_trailers():
    """ screen scrape """
    
    initdb()
    base_url = "http://www.hd-trailers.net/page"
    
    dest_dir = app.config.get('UPLOAD_FOLDER')
    
    for page in range(1, 5):
        page_url = "%s/%d" % (base_url, page)
        list_doc = urllib2.urlopen(page_url).read()
        list_soup = BeautifulSoup(list_doc)
        trs = list_soup.findAll("img", "indexTableTrailerImage")
        for img in trs:
            trailer = Trailer(img['title'])
            db.session.add(trailer)
            db.session.commit()
            urllib.urlretrieve(img['src'], os.path.join(dest_dir, '%s_%d.jpg' % (trailer.slug, trailer.id)))
            
        print "Page", str(page)


if __name__ == "__main__":
    manager.run()
