class Employer:
    '''Модель служащего'''

    def __init__(self, name, age, education):
        self.__name = name
        self.age = age
        self.education = education

    def get_name_employer(self):
        return self.__name

    def get_int_age(self):
        return int(self.age)

    def get_education(self):
        return self.education

    def get_print_infomation_employer(self):
        return ("This is employer class")

    

class President(Employer):

    def __init__(self, name, age, education, post, country):
        super().__init__(name, age, education)
        self.post = post
        self.country = country

    def get_int_age(self):
        return int(self.age)
    def get_post_president(self):
        return self.post

    def get_print_infomation_employer(self):
        return f"Должность: {self.post}\n"\
               f"Страна: {self.country}\n"\
               f"Имя: {super().get_name_employer()}\n"\
               f"Возраст: {self.age}\n"\
               f"Образование: {self.education}"

    def __str__(self):
        return f"Должность: {self.post}\n" \
               f"Страна: {self.country}\n" \
               f"Имя: {super().get_name_employer()}\n" \
               f"Возраст: {self.age}\n" \
               f"Образование: {self.education}"


class Manager(Employer):

    def __init__(self, name, age, education, direction):
        super().__init__(name, age, education)
        self.direction = direction


    def get_int_age(self):
        return int(self.age)
    def get_direction(self):
        return self.direction

    def get_print_infomation_employer(self):
        return f"Имя: {super().get_name_employer()}\n"\
               f"Возраст: {self.age}\n"\
               f"Образование: {self.education}\n"\
               f"Направление: {self.direction}"

    def __str__(self):
        return f"Имя: {super().get_name_employer()}\n" \
               f"Возраст: {self.age}\n" \
               f"Образование: {self.education}\n" \
               f"Направление: {self.direction}"

class Worker(Employer):

    def __init__(self, name, age, education, direction):
        super().__init__(name, age, education)
        self.direction = direction


    def get_int_age(self):
        return int(self.age)
    def get_direction(self):
        return self.direction

    def get_print_infomation_employer(self):
        return f"Имя: {super().get_name_employer()}\n"\
               f"Возраст: {self.age}\n"\
               f"Образование: {self.education}\n"\
               f"Направление: {self.direction}"

    def __str__(self):
        return f"Имя: {super().get_name_employer()}\n" \
               f"Возраст: {self.age}\n" \
               f"Образование: {self.education}\n" \
               f"Направление: {self.direction}"


employer = Employer('Виталий', 21, 'Среднее-Специальное')
print(employer.get_print_infomation_employer())
print()

president = President('Vladimir Putin', 71, 'Высшее', 'President', 'Russia')
print(president)
print()

manager = Manager("Петр Иванов", 28, 'Высшее', 'Продажи')
print(manager)
print()

worker = Worker('Василий Петров', 22, 'Среднее', 'Строительство')
print(worker)