import json


class JSONKeeper:
    @staticmethod
    def make_fill_file(data):
        """
        Статический метод. При первом использовании программы создаёт, в дальнейшем открывает файл, в котором
        храняться вакансии полученные и обработанные пользователем. Выполняется автоматически.

        :param data: Список вакансий после взоимодействия с пользователем.
        """
        with open('data/data.json', 'w') as file:
            for_add_list = []
            for vacancy in data:
                for_add_list.append(vacancy.__dict__)
            json.dump(for_add_list, file, ensure_ascii=False, indent=5)

    @staticmethod
    def delete_vacancies():
        """
        Статический метод. Используется для очистки файла с вакансиями. Выполняется по желанию ппользователя.

        """
        with open('data/data.json', 'w') as file:
            data = None
            json.dump(data, file)
