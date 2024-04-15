import json
from src.parser import HH


class JsonKeeper(HH):

    def __init__(self):
        super().__init__()

    def create_and_fill_json_file(self):
        with open('data/data.json', 'w') as file:
            json.dump(self.vacancies, file, ensure_ascii=False)
