import unittest
from main import DisciplineTeacher
class TestDisciplineTeacher(unittest.TestCase):

    discipline_teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")

    def test_01_discipline_init(self):
        self.assertEqual(len(DisciplineTeacher.discipline_teacher_dict), 1)
        self.assertEqual(DisciplineTeacher.discipline_teacher_dict, {'Иван Петров': ["БГПУ", 4, "Химия", "Директор"]})

    def test_02_discipline_get_discipline(self):
        self.assertEqual(self.discipline_teacher.get_discipline(), 'Химия')

    def test_03_discipline_job_title(self):
        self.assertEqual(self.discipline_teacher.get_job_title(), 'Директор')

    def test_04_discipline_get_teacher_data(self):
        self.assertEqual(self.discipline_teacher.get_teacher_data(), 'Иван Петров, образование БГПУ, опыт работы 4 года,'
                                                                     '\nПредмет Химия, должность Директор\n')

    def test_05_discipline_add_mark(self):
        self.assertEqual(self.discipline_teacher.add_mark("Николай Иванов", 4), 'Иван Петров поставил оценку 4 студенту Николай Иванов.\n'
                                                                                         'Предмет Химия\n')

    def test_06_discipline_remove_mark(self):
        self.assertEqual(self.discipline_teacher.remove_mark("Дмитрий Сидоров", 3), 'Иван Петров, удалил оценку 3 студенту Дмитрий Сидоров.\nПредмет Химия\n')

    def test_07_discipline_give_a_consultation(self):
        self.assertEqual(self.discipline_teacher.give_a_consultation('10 Б'), 'Иван Петров провел консультацию в классе 10 Б.\n'
                                                                                       'По предмету Химия как Директор\n')

