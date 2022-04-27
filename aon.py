import importlib
import sys
from os import listdir
from os.path import isfile, join, dirname

import_all_api = [f for f in listdir(join(dirname(__file__), "API")) if isfile(join("API", f))]
API_CHECK = []
for i in range(len(import_all_api)):
    API_CHECK.append(importlib.import_module("API." + import_all_api[i][0:-3]))

def all_check(numbers_phone):
    for x in range(len(API_CHECK)):
        print(str(API_CHECK[x].name()) + ": " + str(API_CHECK[x].main(numbers_phone)))

def check(numbers_phone):
    for x in range(len(API_CHECK)):
        if API_CHECK[x].main(numbers_phone):
            return True
            #break
    return API_CHECK

def check_sel(numbers_phone, API_NAME):
    for x in range(len(API_CHECK)):
        if API_CHECK[x].name() == API_NAME:
            return API_CHECK[x].main(numbers_phone)
            #break
    return False