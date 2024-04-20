from src.vacancies import Vacancy
from src.parser import HH
from src.jsonkeeper import JSONKeeper


def get_filtered_vacancies_by_city(vacancies_list, user_city):
    """
    Функция фильтрует список вакансий по городу, который укажет пользователь.

    :param vacancies_list: Лист с нефильтрованными вакансиями.
    :param user_city: Введённый город для фильтрации.
    :return: Отфильтрованный список вакансий.
    """
    filtered_by_city_list = []
    for vacancy in vacancies_list:
        if user_city.lower() in vacancy.city.lower():
            filtered_by_city_list.append(vacancy)

    return filtered_by_city_list


def get_sorted_vacancies(vacancies_list):
    """
    Функция сортирует список вакансия по минимальной зарплате.

    :param vacancies_list: Список вакансий до сортировки.
    :return: Сортированный список вакансий.
    """
    return sorted(vacancies_list, reverse=True)


def get_top_n_by_salary(vacancies_list, n):    # use after (get_sorted_vacancies)
    """
    Функция выводит срез вакансий. В колличестве, указанном пользователем.

    :param vacancies_list: Список вакансий.
    :param n: Стоп-число среза. Вводит пользоваетель.
    :return: Срез вакансий. Представляет собой топ, так как функцитя используется после сортировки, что указано выше.
    """
    return vacancies_list[:n]


def user_interaction():
    """
    Функция является пользовательским интерфейсом для рабботы с программой.
    """
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
            JSONKeeper.make_fill_file(vacancies_list)
            save_notsave = input('Данные автоматически сохранены в файл. Чтобы отменить сохранение - напишите "да"\n'
                                 'Иначе - нажмите Enter\n')
            if save_notsave.lower() == 'да':
                JSONKeeper.delete_vacancies()
            continue
        elif int(user_input) == 2:
            user_city = input('Введите город для фильтрации: ')
            filtered_by_city_list = get_filtered_vacancies_by_city(vacancies_list, user_city)
            Vacancy.print_vacancies(filtered_by_city_list)
            JSONKeeper.make_fill_file(filtered_by_city_list)
            save_notsave = input('Данные автоматически сохранены в файл. Чтобы отменить сохранение - напишите "да"\n'
                                 'Иначе - нажмите Enter\n')
            if save_notsave.lower() == 'да':
                JSONKeeper.delete_vacancies()
            continue
        elif int(user_input) == 3:
            user_n = int(input('Введите число-ограничитель топа: '))
            sorted_list = get_sorted_vacancies(vacancies_list)
            top_n_vacancies = get_top_n_by_salary(sorted_list, user_n)
            Vacancy.print_vacancies(top_n_vacancies)
            JSONKeeper.make_fill_file(top_n_vacancies)
            save_notsave = input('Данные автоматически сохранены в файл. Чтобы отменить сохранение - напишите "да"\n'
                                 'Иначе - нажмите Enter\n')
            if save_notsave.lower() == 'да':
                JSONKeeper.delete_vacancies()
            continue
        elif int(user_input) == 4:
            user_city = input('Введите город для фильтрации: ')
            user_n = int(input('Введите число-ограничитель топа: '))
            filtered_by_city_list = get_filtered_vacancies_by_city(vacancies_list, user_city)
            sorted_list = get_sorted_vacancies(filtered_by_city_list)
            top_n_vacancies = get_top_n_by_salary(sorted_list, user_n)
            Vacancy.print_vacancies(top_n_vacancies)
            JSONKeeper.make_fill_file(top_n_vacancies)
            save_notsave = input('Данные автоматически сохранены в файл. Чтобы отменить сохранение - напишите "да"\n'
                                 'Иначе - нажмите Enter\n')
            if save_notsave.lower() == 'да':
                JSONKeeper.delete_vacancies()
            continue
        else:
            print('Такого пункта в меню нет.')
            continue
