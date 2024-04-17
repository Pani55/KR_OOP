from src.parser import HH
from src.vacancies import Vacancy
from src.utils import get_filtered_vacancies_by_city, get_sorted_vacancies


user_keyword = input('Введите профессию: ')
user_city = input('Введите город: ')

hh_api = HH()

hh_vacancies = hh_api.load_vacancies(user_keyword)

vacancies_list = Vacancy.cost_to_object_list(hh_vacancies)
vacancies_list = get_filtered_vacancies_by_city(vacancies_list, user_city)
vacancies_list = get_sorted_vacancies(vacancies_list)

for i in vacancies_list:
    print(i)
