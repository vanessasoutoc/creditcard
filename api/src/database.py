from mongoengine import connect
import os

connect("mongoengine", host=os.environ['DATABASE_URL'])
