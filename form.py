import re
import time
import datetime
import mechanize
import requests
from mms import send_mms
from bs4 import BeautifulSoup


def check_variables(accessid, phone_num, phone_provider):
    check_accessid = bool(re.match("[A-Za-z]{2}\\d{4}\\Z", accessid))
    if not check_accessid:
        print("Your AccessID is incorrect.")
    check_phone_num = bool(re.match("\\d{10}\\Z", phone_num))
    if not check_phone_num:
        print("Your phone number is incorrect.")
    with open("phone_providers.txt", "r") as f:
        phone_providers_list = f.read().splitlines()
    check_phone_provider = phone_provider in phone_providers_list
    if not check_phone_provider:
        print("Your phone provider is incorrect.")
    return check_accessid and check_phone_num and check_phone_provider


def sleep():
    today = datetime.datetime.now()
    sleep_time = (
        datetime.datetime(
            today.year,
            today.month,
            today.day,
            0,
            0,
            0) -
        today).seconds
    print(f"Waiting for {datetime.timedelta(seconds=sleep_time)}")
    time.sleep(sleep_time)


def login_and_fill_form(accessid, password, phone_num, phone_provider):
    if not check_variables(accessid, phone_num, phone_provider):
        return
    sleep()
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [
        ('User-agent',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')]
    link = "https://forms.wayne.edu/covid-19-screening"
    br.open(link)
    br.select_form(nr=1)
    br.form['accessid'] = accessid
    br.form['passwd'] = password
    br.submit()
    br.select_form(nr=1)
    br.form['f_253006'] = phone_num
    br.form['f_253229[]'] = ['1000']
    br.form['f_251741'] = ['No']
    br.form['f_251742'] = ['No']
    br.form['f_255927'] = ['No']
    br.submit()
    print(get_screenshot(br, phone_num, phone_provider))


def get_screenshot(br, phone_num, phone_provider):
    page_html = br.response().read()
    soup = BeautifulSoup(page_html, 'html.parser')
    images = soup.findAll('img')
    if len(images) == 0:
        return soup.find("p", {"id": "error-message-f_253006"}).text
    for image in images:
        image_link = image['src']
        if "chart.apis.google.com" in image_link:
            break
    response = requests.get(image_link)
    with open("screenshot.png", "wb") as f:
        f.write(response.content)
    submitted_on = [text.text.strip("\n").strip()
                    for text in soup.findAll('p')][4]
    send_mms(phone_num, submitted_on, "screenshot.png", "", phone_provider)
    return submitted_on
