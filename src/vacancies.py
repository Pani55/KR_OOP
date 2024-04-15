class Vacancies:

    def __init__(self, name, area, requirement, salary_from: None, salary_to: None, alternate_url):
        if salary_from is None:
            self.salary_from = 0
        else:
            self.salary_from = salary_from
        if salary_to is None:
            self.salary_to = 0
        else:
            self.salary_to = salary_to

        self.name = name
        self.area = area
        self.requirement = requirement
        self.url = alternate_url

    def __repr__(self):
        return (f"{self.name}, {self.area}, {self.requirement},"
                f" {self.salary_from}, {self.salary_to}, {self.url}")
