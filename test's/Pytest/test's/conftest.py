import pytest

from main import Teacher, DisciplineTeacher

@pytest.fixture
def teacher_fixture():
    Teacher.teacher_dict.clear()
    teacher = Teacher('Иван Петров', 'БГПУ', 4, None)
    return teacher

@pytest.fixture
def discipline_teacher_fixture():
    DisciplineTeacher.discipline_teacher_dict.clear()
    discipline_teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
    return discipline_teacher