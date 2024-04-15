class Vacancies:

    def __init__(self, name, area, requirement, salary_from, salary_to, alternate_url):
        self.name = name
        self.area = area
        self.requirement = requirement
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = alternate_url

    def __repr__(self):
        return (f"{self.name}, {self.area}, {self.requirement},"
                f" {self.salary_from}, {self.salary_to}, {self.url}")
