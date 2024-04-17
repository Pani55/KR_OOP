from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': '', 'per_page': 100}
        self.vacancies = None

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        response = requests.get(self.url, params=self.params)
        self.vacancies = response.json()['items']

        return self.vacancies
