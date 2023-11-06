from mongoengine import Document, StringField, DateField
from bson.objectid import ObjectId

class CreditCard(Document):
    id = StringField(primary_key=True, default=lambda:str(ObjectId()))
    number = StringField(length=16,required=True,unique=True)
    exp_date = DateField(required=True)
    holder = StringField(max_length=99, required=True)
    cvv = StringField(length=3,required=True)
    brand = StringField(max_length=30, required=True)
