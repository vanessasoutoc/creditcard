from mongoengine import *

class CreditCard(DynamicDocument):
    number = StringField(length=16,required=True,unique=True)
    exp_date = DateField(required=True)
    holder = StringField(max_length=99, required=True)
    cvv = StringField(length=3,required=True)
    brand = StringField(max_length=30, required=True)
