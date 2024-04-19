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


def user_interaction():
    hh_api = HH()

    print('Добрый день! Вы используете интерфейс для работы с API HeadHunter.')
    user_keyword = input('Введите профессию: ')

    hh_vacancies = hh_api.load_vacancies(user_keyword)
    vacancies_list = Vacancy.cost_to_object_list(hh_vacancies)
    while True:
        user_input = input('||||||||||||||||||||||||||||||||||||||||||||||||||||\n'
                           'Перед вами меню взоимодействия с интерфейсом.\n'
                           'Введите:\n'
                           '1 => Вывести все вакансии по профессии.\n'
                           '2 => Вывести вакансии, отфильтрованные по городу.\n'
                           '3 => Вывести топ N вакансий по минимальной зарплате\n'
                           '4 => Всё и сразу!!!\n'
                           '||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
        if user_input.lower() in ('stop', 'стоп'):
            exit('Вы закрыли приложение!'
                 'Спасибо, что воспользовались!')
        elif int(user_input) == 1:
            Vacancy.print_vacancies(vacancies_list)
            continue
        elif int(user_input) == 2:
            user_city = input('Введите город для фильтрации: ')
            filtered_by_city_list = get_filtered_vacancies_by_city(vacancies_list, user_city)
            Vacancy.print_vacancies(filtered_by_city_list)
            continue
        elif int(user_input) == 3:
            user_n = int(input('Введите число-ограничитель топа: '))
            sorted_list = get_sorted_vacancies(vacancies_list)
            top_n_vacancies = get_top_n_by_salary(sorted_list, user_n)
            Vacancy.print_vacancies(top_n_vacancies)
            continue
        elif int(user_input) == 4:
            user_city = input('Введите город для фильтрации: ')
            user_n = int(input('Введите число-ограничитель топа: '))
            filtered_by_city_list = get_filtered_vacancies_by_city(vacancies_list, user_city)
            sorted_list = get_sorted_vacancies(filtered_by_city_list)
            top_n_vacancies = get_top_n_by_salary(sorted_list, user_n)
            Vacancy.print_vacancies(top_n_vacancies)
            continue
        else:
            print('Такого пункта в меню нет.')
            continue