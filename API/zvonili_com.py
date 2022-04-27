import requests
from bs4 import BeautifulSoup

count = 3 # Мин. низкая оценка если является спам-номер

def name():
    return "zvonili_com"

def main(number):

    if number[0:2] != "+7":
        return False

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    }

    get_page = requests.get('https://zvonili.com/phone/' + number, headers=headers).text

    result = BeautifulSoup(get_page, 'html.parser').body.find_all("table", "mb-3")

    if not result:
        return False

    result = result[0].find_all("td")[1].span.text.split("/")[0]

    if float(result) == 0:
        return False
    elif float(result) >= count:
        return False
    else:
        return True