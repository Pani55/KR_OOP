from src.json_keeper import JsonKeeper


user_keyword = input('Введите профессию: ')
exp1 = JsonKeeper()
exp1.load_vacancies(user_keyword)
print(exp1.vacancies)
exp1.create_and_fill_json_file()