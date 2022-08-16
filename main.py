import os
from form import login_and_fill_form
from mechanize import ControlNotFoundError

try:
    accessid = os.environ["accessid"]
    password = os.environ["password"]
    phone_num = os.environ["phone_num"]
    phone_provider = os.environ["phone_provider"]
except KeyError as k:
    print(f"The variable {k} is missing.")
    
try:
    login_and_fill_form(accessid, password, phone_num, phone_provider)
except ControlNotFoundError:
     print(
        "The AccessID and password entered do not match.")