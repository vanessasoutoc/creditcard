from mongoengine import connect
import os

class MongoClient():
    def __init__(self):
        self.connection = connect(
                "creditcard",
                host=os.environ['DATABASE_URL'],
                uuidRepresentation='standard'
            )

    def close(self):
        self.connection.close()


