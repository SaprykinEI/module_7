

from main import DisciplineTeacher

def test_01_init(discipline_teacher_fixture):
    assert len(DisciplineTeacher.discipline_teacher_dict) == 1
    assert DisciplineTeacher.discipline_teacher_dict == {'Иван Петров': ["БГПУ", 4, "Химия", "Директор"]}


def test_02_get_discipline(discipline_teacher_fixture):
    assert discipline_teacher_fixture.get_discipline() == 'Химия'


def test_03_get_job_title(discipline_teacher_fixture):
    assert discipline_teacher_fixture.get_job_title() == 'Директор'


def test_04_set_job_tittle(discipline_teacher_fixture):
    discipline_teacher_fixture.set_job_title('Учитель')
    assert discipline_teacher_fixture.get_job_title() == 'Учитель'

def test_05_get_teacher_data(discipline_teacher_fixture):
    assert discipline_teacher_fixture.get_teacher_data() == ('Иван Петров, образование БГПУ, опыт работы 4 года,'
                                                             '\nПредмет Химия, должность Директор\n')


def test_06_add_mark(discipline_teacher_fixture):
    assert discipline_teacher_fixture.add_mark("Николай Иванов", "4") == ('Иван Петров поставил оценку 4 студенту Николай Иванов.\n'
                                                                          'Предмет Химия\n')


def test_07_remove_mark(discipline_teacher_fixture):
    assert discipline_teacher_fixture.remove_mark("Дмитрий Сидоров", "3") == 'Иван Петров, удалил оценку 3 студенту Дмитрий Сидоров.\nПредмет Химия\n'


def test_08_give_a_consultation(discipline_teacher_fixture):
    assert discipline_teacher_fixture.give_a_consultation('10 Б') == ('Иван Петров провел консультацию в классе 10 Б.\n'
                                                                      'По предмету Химия как Директор\n')