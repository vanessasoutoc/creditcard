from datetime import datetime
import calendar
from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound
import re


def is_valid_card(number: str):
    return CreditCard(number).is_valid()

def brand_card(number: str):
    try:
        return CreditCard(number).get_brand()
    except BrandNotFound as error:
        raise error

def exp_date_format(date: str):
    date_format = datetime.strptime(date, '%m/%Y').date()
    last_day = calendar.monthrange(date_format.year, date_format.month)[1]
    return str(datetime(date_format.year, date_format.month, last_day).date())

def validate_exp_date(exp_date: str):
    if bool(re.match("(\d{2})[/](\d{4})$", exp_date)) != True:
        raise ValueError('exp_date not valid')
    return True



