class Teacher:
    '''Модель преподавателя'''
    teacher_dict = {}

    def __init__(self, name, education, experience, discipline):
        self.__name = name
        self.__education = education
        self.__experience = experience
        self.__discipline = discipline
        Teacher.teacher_dict[self.__name] = [self.__education, self.__experience, self.__discipline]

    def get_teacher_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience


    def get_discipline(self):
        return self.__discipline

    def get_teacher_data(self):
        return f"{self.get_teacher_name()}, образование {self.get_education()}, опыт работы {self.get_experience()} года"

    def add_mark(self, student_name, estimation):
        return f"{self.get_teacher_name()} поставил оценку {estimation} студенту {student_name}"

    def remove_mark(self, student_name, estimation):
        return f"{self.get_teacher_name()}, удалил оценку {estimation} студенту {student_name}"

    def give_a_consultation(self, student_class):
        return f"{self.get_teacher_name()} провел консультацию в классе {student_class}"

    def fire_teacher(self):
        if self.__name in Teacher.teacher_dict:

            Teacher.teacher_dict.pop(self.__name)
            return f"Сотрудник {self.__name} был уволен"
        else:
            return f"Сотрудника {self.__name} уже уволили"


class DisciplineTeacher(Teacher):
    '''Модель Преподавателя по предмету'''
    discipline_teacher_dict = {}

    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience, discipline)
        self.__job_title = job_title
        DisciplineTeacher.discipline_teacher_dict[name] = [education,
                                             experience,
                                             discipline, self.__job_title]

    def get_discipline(self):
        return super().get_discipline()

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        data = super().get_teacher_data()
        return f"{data},\nПредмет {Teacher.get_discipline(self)}, должность {self.__job_title}\n"


    def add_mark(self, student_name, estimation):
        data = super().add_mark(student_name, estimation)
        return f"{data}.\nПредмет {self.get_discipline()}\n"

    def remove_mark(self, student_name, estimation):
        super().remove_mark(student_name, estimation)
        return (f"{self.get_teacher_name()}, удалил оценку {estimation} студенту {student_name}.\n"
                f"Предмет {self.get_discipline()}\n")

    def give_a_consultation(self, student_class):
        super().give_a_consultation(student_class)
        return (f"{self.get_teacher_name()} провел консультацию в классе {student_class}.\n"
                f"По предмету {self.get_discipline()} как {self.__job_title}\n")



# teach = Teacher('Иван Петров', 'БГПУ', 4, None)
# print(teach.get_teacher_data())
# print(teach.add_mark('Петр Сидоров', 4))
# print(teach.remove_mark('Дмитрий Степанов', 3))
# print(teach.give_a_consultation('9Б'))
# teach.set_experience(5)
# print(teach.get_teacher_data())
# print(teach.fire_teacher())
# print(teach.fire_teacher())
# print()
#
#
# director = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
# print(director.get_teacher_data())
# print(director.add_mark("Николай Иванов", "4"))
# print(director.remove_mark("Дмитрий Сидоров", "3"))
# print(director.give_a_consultation("10 Б"))
# print()
# director.set_job_title("Учитель")
# print(director.get_teacher_data())
# print(director.give_a_consultation("10 Б"))