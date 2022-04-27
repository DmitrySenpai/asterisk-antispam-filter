import requests
from bs4 import BeautifulSoup

count = 2 # Мин. низкая оценка если является спам-номер

def name():
    return "neberitrubku_com"

def main(number):

    if number[0:2] != "+7":
        return False

    get_page = requests.get('https://neberitrubku.com/' + number).text
    check_status = BeautifulSoup(get_page, 'html.parser').body.find_all("div", "assessment")
    if not check_status:
        return False
    result = check_status[0].find_all("span", "assessment__number")[0].text
    result = result.split("/")[0]
    if int(result) == 0:
        return False
    elif int(result) >= count:
        return False
    else:
        return True