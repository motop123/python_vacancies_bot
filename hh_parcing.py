import requests
import time
import json

def get_page(page = 0):
    params = {
        'text': 'python',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 16,  # Поиск ощуществляется по вакансиям города Минск
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100,  # Кол-во вакансий на 1 странице
        'period': 1
    }
    req = requests.get('https://api.hh.ru/vacancies', params=params)
    data = req.content.decode()
    req.close()
    return data

def parce_data():
    lst_Obj = []

    for i in range(11):
        json_data = get_page(i)
        jsObj = json.loads(json_data)
        lst_Obj.extend(jsObj['items'])
        time.sleep(0.25)
    return lst_Obj


