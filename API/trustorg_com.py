import requests
from bs4 import BeautifulSoup

def name():
    return "trustorg_com"

def main(number):

    if number[0:2] != "+7":
        return False

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    }

    get_page = requests.get('https://trustorg.com/phone/' + number[1:], headers=headers).text
    check_status = BeautifulSoup(get_page, 'html.parser').body.find_all("div", "main_center")[0].img

    if not check_status:
        return False

    check_status = check_status['src']
    match check_status:
        case '/img/light/t_yellow.png':
            return True
        case '/img/light/t_grey.png':
            return False
        case '/img/light/t_blue.png':
            return False

    return False