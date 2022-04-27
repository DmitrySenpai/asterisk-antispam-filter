import requests
from bs4 import BeautifulSoup

def name():
    return "phoneradar_ru"

def main(number):

    if number[0:2] != "+7":
        return False

    get_page = requests.get('http://phoneradar.ru/phone/' + number).text
    result = BeautifulSoup(get_page, 'html.parser').body.find_all("div", "card-body")[0].find_all("table", "table")
    
    if not result:
        return False

    result = result[0].find_all("td")
    rating = [int(result[11].text), int(result[13].text), int(result[15].text)]
    #11 - Положительные
    #13 - Отрицательные
    #15 - Нейтральные

    if rating[0] >= rating[1]:
        return False
    else:
        return True