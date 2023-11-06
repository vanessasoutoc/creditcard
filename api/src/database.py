from mongoengine import connect
import os

class MongoClient():
    def __init__(self):
        self.connection = connect("creditcard", host=os.environ['DATABASE_URL'])

    def close(self):
        self.connection.close()


