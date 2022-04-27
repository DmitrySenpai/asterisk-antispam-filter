import requests
from bs4 import BeautifulSoup

def name():
    return "callfilter_app"

def main(number):

    if number[0:2] != "+7":
        return False

    get_page = requests.get('https://callfilter.app/' + number[1:]).text
    check_status = BeautifulSoup(get_page, 'html.parser').body.find_all("div", "scoreContainer")[0].div['class'][1]

    if check_status == "negative":
        return True
    else:
        return False