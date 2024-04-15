import json
from src.json_keeper import JsonKeeper
from src.vacancies import Vacancies


vacancies_list = []
user_keyword = input('Введите профессию: ')

exp1 = JsonKeeper()
exp1.load_vacancies(user_keyword)
exp1.create_and_fill_json_file()


with open('data/data.json', 'r') as file:
    info = json.load(file)

    for i in info:
        vacancies_list.append(Vacancies(i['name'], i['area']['name'], i['snippet']['requirement'],
                                        i['salary']['from'], i['salary']['to'], i['alternate_url']))

for k in vacancies_list:
    print(type(k))
