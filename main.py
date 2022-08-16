import os
from functions import login_and_fill_form
from mechanize import ControlNotFoundError

accessid = os.environ["accessid"]
password = os.environ["password"]
phone_num = os.environ["phone"]
phone_provider = os.environ["phone_provider"]

try:
    login_and_fill_form(accessid, password, phone_num, phone_provider)
except ControlNotFoundError:
     print(
        "The AccessID and password you have entered do not match.")