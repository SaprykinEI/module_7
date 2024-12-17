from main import Teacher


def test_01_teacher_init(teacher_fixture):
    assert len(Teacher.teacher_dict) == 1
    assert Teacher.teacher_dict == {'Иван Петров': ['БГПУ', 4, None]}


def test_02_get_teacher_name(teacher_fixture):
    assert teacher_fixture.get_teacher_name() == "Иван Петров"


def test_03_get_education(teacher_fixture):
    assert teacher_fixture.get_education() == 'БГПУ'


def test_04_get_experience(teacher_fixture):
    assert teacher_fixture.get_experience() == 4


def test_05_get_discipline(teacher_fixture):
    assert teacher_fixture.get_discipline() == None


def test_06_get_teacher_data(teacher_fixture):
    assert teacher_fixture.get_teacher_data() == 'Иван Петров, образование БГПУ, опыт работы 4 года'


def test_07_add_mark(teacher_fixture):
    assert  teacher_fixture.add_mark('Петр Сидоров', 4) == 'Иван Петров поставил оценку 4 студенту Петр Сидоров'


def test_08_remove_mark(teacher_fixture):
    assert teacher_fixture.remove_mark('Дмитрий Степанов', 3) == 'Иван Петров, удалил оценку 3 студенту Дмитрий Степанов'


def test_09_give_a_consultation(teacher_fixture):
    assert teacher_fixture.give_a_consultation('9Б') == 'Иван Петров провел консультацию в классе 9Б'


def test_10_fire_teacher(teacher_fixture):
    assert teacher_fixture.fire_teacher() == "Сотрудник Иван Петров был уволен"
    assert teacher_fixture.fire_teacher() == "Сотрудника Иван Петров уже уволили"