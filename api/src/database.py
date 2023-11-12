import os
from dotenv import load_dotenv
from mongoengine import connect

load_dotenv()

class MongoClient():
    def __init__(self):
        self.connection = connect(
                "creditcard",
                host=os.getenv('MONGO_DB'),
                uuidRepresentation='standard',
            )
