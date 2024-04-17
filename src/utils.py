from src.parser import HH
from src.vacancies import Vacancy


def get_filtered_vacancies_by_city(vacancies_list, user_city):
    filtered_by_city_list = []
    for vacancy in vacancies_list:
        if user_city.lower() in vacancy.city.lower():
            filtered_by_city_list.append(vacancy)

    return filtered_by_city_list


def get_sorted_vacancies(vacancies_list):
    return sorted(vacancies_list, reverse=True)
