from mongoengine import connect
import os

class MongoClient():
    def __init__(self):
        self.connection = connect(
                "creditcard",
                host='mongodb://creditcard:creditcard@mongodb:27017',
                uuidRepresentation='standard',
            )

    def close(self):
        self.connection.close()


