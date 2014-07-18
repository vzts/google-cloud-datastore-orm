import os
import sys

def include_sys(paths):
    for p in paths:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), p))

include_sys([
    'lib/gcloud-python',
    'lib/google-cloud-datastore/python',
    'lib/google_appengine',
])

import google
google.__path__.append(os.path.join('lib', 'google'))

import googledatastore as datastore
datastore.set_options(dataset="tagtooadex2")
os.environ["APPLICATION_ID"] = "tagtooadex2"
import datastore_rpc
import google.appengine.datastore
google.appengine.datastore.datastore_rpc = datastore_rpc
from google.appengine.ext import db

class Test(db.Model):
    test_int = db.IntegerProperty()
    test_string = db.TextProperty()

t = Test.get_by_key_name('test')

# print sys.modules.keys()
