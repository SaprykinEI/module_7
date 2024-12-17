import unittest
from main import Teacher

class TestTeacher(unittest.TestCase):

    teacher = Teacher('Иван Петров', 'БГПУ', 4, None)

    def test_01_init(self):
        self.assertEqual(len(Teacher.teacher_dict), 1)
        self.assertEqual(Teacher.teacher_dict, {'Иван Петров': ['БГПУ', 4, None]})

    def test_02_get_teacher_name(self):
        self.assertEqual(self.teacher.get_teacher_name(), 'Иван Петров')

    def test_03_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'БГПУ')

    def test_04_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 4)

    def test_05_get_discipline(self):
        self.assertEqual(self.teacher.get_discipline(), None)

    def test_06_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), 'Иван Петров, образование БГПУ, опыт работы 4 года')

    def test_07_add_mark(self):
        self.assertEqual(self.teacher.add_mark('Петр Сидоров', 4), 'Иван Петров поставил оценку 4 студенту Петр Сидоров')

    def test_08_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark("Дмитрий Сидоров", 3), 'Иван Петров, удалил оценку 3 студенту Дмитрий Сидоров')

    def test_09_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('10 Б'), 'Иван Петров провел консультацию в классе 10 Б')

    def test_10_fire_teacher(self):
        self.assertEqual(self.teacher.fire_teacher(), 'Сотрудник Иван Петров был уволен')
        self.assertEqual(self.teacher.fire_teacher(), 'Сотрудника Иван Петров уже уволили')
        self.assertEqual(Teacher.teacher_dict, {})