# Asterisk antispam filter

**Работает только с кодами +7!**

Этот скрипт сможет определить является спам номер или нет. 

## Используються сайты
- callfilter.app
- neberitrubku.com
- phoneradar.ru
- trustorg.com
- zvonili.com

## Создание доп. API

В папке **API** создайте файл с расширение *.py* (При этом, название файла не должно содержаться русские символы!).

Простой пример скрипта:
```python
def name():
    #Название API
    return "simple_file"

def main(number):
    # ... here code
    if result:
        # Является спам номером
        return True
    else:
        # Не является
        return False
```
