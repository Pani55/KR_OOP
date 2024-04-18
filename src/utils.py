from src.vacancies import Vacancy
from src.parser import HH


def get_filtered_vacancies_by_city(vacancies_list, user_city):
    filtered_by_city_list = []
    for vacancy in vacancies_list:
        if user_city.lower() in vacancy.city.lower():
            filtered_by_city_list.append(vacancy)

    return filtered_by_city_list


def get_sorted_vacancies(vacancies_list):
    return sorted(vacancies_list, reverse=True)


def get_top_n_by_salary(vacancies_list, n):    # use after (get_sorted_vacancies)
    return vacancies_list[:n]


"""def user_interaction():
    hh_api = HH()

    print('Добрый день! Вы используете интерфейс для работы с API HeadHunter.')
    user_keyword = input('Введите профессию')

    hh_vacancies = hh_api.load_vacancies(user_keyword)
    vacancies_list = Vacancy.cost_to_object_list(hh_vacancies)
    while user_input not in 'стоп' or 'stop':
        user_input = input('Перед вами меню взоимодействия с интерфейсом.'
              'Введите:'
              '1 => Вывести все вакансии по профессии.'
              '2 => Вывести вакансии, отфильтрованные по городу.'
              '3 => Вывести топ N вакансий по минимальной зарплате'
              '4 => Всё и сразу!!!')
        if 
"""
