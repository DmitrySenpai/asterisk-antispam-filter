import aon
import os
import sys
CACHE = True


def start(number_phone):
    if CACHE:
        if os.path.isfile('cache.txt'):
            cache_number = open('cache.txt', 'r+')
            cache_number_read = cache_number.read().split(',')
            if number_phone in cache_number_read:
                return True
        else:
            cache_number = open('cache.txt', 'a')

    if aon.check(number_phone) == True:
        if CACHE:
            cache_number.write(number_phone + ',')
            cache_number.close()
        return True
    else:
        return False


if sys.argv[1][0:2] == "+7":
    print(start(sys.argv[1]))