from src.parser import HH
from src.vacancies import Vacancy
from src.utils import get_filtered_vacancies_by_city, get_sorted_vacancies, get_top_n_by_salary


user_keyword = input('Введите профессию: ')
user_city = input('Введите город: ')
user_top_n = int(input('Введите кол-во вакансий: '))

hh_api = HH()

hh_vacancies = hh_api.load_vacancies(user_keyword)

vacancies_list = Vacancy.cost_to_object_list(hh_vacancies)
filtered_list = get_filtered_vacancies_by_city(vacancies_list, user_city)
sorted_list = get_sorted_vacancies(filtered_list)
top_n = get_top_n_by_salary(sorted_list, user_top_n)


Vacancy.print_vacancies(top_n)
