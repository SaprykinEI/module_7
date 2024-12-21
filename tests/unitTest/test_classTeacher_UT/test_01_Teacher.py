import unittest
from main import Teacher, DisciplineTeacher

class TestTeacher(unittest.TestCase):

    teacher = Teacher('name', 'education', 'experience', 'discipline')

    def test_01_init(self):
        self.assertEqual(len(Teacher.teacher_dict), 1)
        self.assertEqual(Teacher.teacher_dict, {'name': ['education', 'experience', 'discipline']})

    def test_02_get_teacher_name(self):
        self.assertEqual(self.teacher.get_teacher_name(), 'name')

    def test_03_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'education')

    def test_04_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 'experience')

    def test_05_get_discipline(self):
        self.assertEqual(self.teacher.get_discipline(), 'discipline')

    def test_06_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), 'name, образование education, опыт работы experience года')

    def test_07_add_mark(self):
        self.assertEqual(self.teacher.add_mark('name', 'estimation'), 'name поставил оценку estimation студенту name')

    def test_08_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('name', ' estimation'), 'name, удалил оценку  estimation студенту name')

    def test_09_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('student class'), 'name провел консультацию в классе student class')

    def test_10_fire_teacher(self):
        self.assertEqual(self.teacher.fire_teacher(), 'Сотрудник name был уволен')
        self.assertEqual(self.teacher.fire_teacher(), 'Сотрудника name уже уволили')
        self.assertEqual(Teacher.teacher_dict, {})

    def test_11_set_experience(self):
        self.teacher.set_experience(5)
        self.assertEqual(self.teacher.get_experience(), 5)


class TestDisciplineTeacher(unittest.TestCase):

    discipline_teacher = DisciplineTeacher('name', 'education', 'experience', 'discipline', 'job_title')

    def test_01_discipline_init(self):
        self.assertEqual(len(DisciplineTeacher.discipline_teacher_dict), 1)
        self.assertEqual(DisciplineTeacher.discipline_teacher_dict, {'name': ['education', 'experience', 'discipline', 'job_title']})

    def test_02_discipline_get_discipline(self):
        self.assertEqual(self.discipline_teacher.get_discipline(), 'discipline')

    def test_03_discipline_job_title(self):
        self.assertEqual(self.discipline_teacher.get_job_title(), 'job_title')

    def test_04_discipline_get_teacher_data(self):
        self.assertEqual(self.discipline_teacher.get_teacher_data(), 'name, образование education, опыт работы experience года,\nПредмет discipline, должность job_title\n')

    def test_05_discipline_add_mark(self):
        self.assertEqual(self.discipline_teacher.add_mark('student_name', 'estimation'), 'name поставил оценку estimation студенту student_name.\nПредмет discipline\n')

    def test_06_discipline_remove_mark(self):
        self.assertEqual(self.discipline_teacher.remove_mark('student_name', 'estimation'), 'name, удалил оценку estimation студенту student_name.\nПредмет discipline\n')

    def test_07_discipline_give_a_consultation(self):
        self.assertEqual(self.discipline_teacher.give_a_consultation('student_class'), 'name провел консультацию в классе student_class.\nПо предмету discipline как job_title\n')