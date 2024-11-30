from datetime import date

class Football_club:
    '''Модель футбольного клуба'''

    def __init__(self, name_club, president, head_coach, budget, team=None, name_stadion=None):
        self.name_club = name_club
        self.president = president
        self.head_coach = head_coach
        self.team = team
        self.budget = budget
        self.name_stadion = name_stadion


    def get_information_about_the_club(self, nickname, country, colors_club, date_of_creation, trophies: list=None):
        '''Вывод информации о клубе'''
        return (f"Название клуба: {self.name_club}\n"
                f"Страна: {country}\n"
                f"Прозвище: {nickname}\n"
                f"Президент: {self.president}\n"
                f"Стадион: {self.name_stadion}\n"
                f"Цвета клуба: {colors_club}\n"
                f"Дата основания: {date_of_creation}\n"
                f"Трофеи: {trophies}\n")


    def get_coaching_staff(self, assistant_coach):
        "Выводит информацию о тренерском штабе"
        return (f"Главный тренер: {self.head_coach}\n"
                f"Помощник главного тренера: {assistant_coach}")


    def get_budget_of_club(self):
        '''Бюджет клуба '''
        budget_club = self.budget
        return f"Бюджет клуба {self.name_club}: {budget_club}"







class Scouting_departament(Football_club):
    '''Скаутский отдел футбольного клуба'''

    def __init__(self, new_player, name_club, president, head_coach, budget, team, name_stadion=None):
        super().__init__(name_club, president, head_coach, budget, team)
        self.new_player = new_player
        self.transfer_amount = 0


    def get_transfer_request(self, player_amount):
        '''Запрос на трансфер'''

        self.transfer_amount += player_amount
        return (f"В скаутский отдел ФК {self.name_club}, пришёл запрос от нашего главного тренера {self.head_coach}.\n"
                f"Он просит рассмотреть возможность покупки нового игрока {self.new_player}, что бы повысить конкуренцию в клубе\n"
                f"и усилить позицию на поле.\n"
                f"Стоимость игрока: {player_amount}\n")


    def get_transfer_decision(self):
        '''Анализ трансферного предложения'''

        transfer_budget = (self.budget / 100) * 15


        if self.transfer_amount > transfer_budget:
            return (f"На нынешний год на трансферы мы не можем потратить больше {transfer_budget} $,"
                    f"Нам не хвататет бюджета на {self.new_player}, к сожалению вынуждены отклонить Ваш запрос Mr.{self.head_coach}")

        elif self.transfer_amount == transfer_budget:
            self.budget = self.budget - self.transfer_amount
            return f"Мы можем себе позволить подписать {self.new_player}, но учтите что это все деньги на этот год!"

        elif self.transfer_amount < transfer_budget:
            self.budget = self.budget - self.transfer_amount
            return (f"Отличный вариант. Вступайте в переговоры с {self.new_player}\n")




my_club = Football_club('Барселона', 'Жоан Лапорта', 'Ханс-Дитер Флик', 800_000_000, 'Камп Ноу')
print(my_club.get_information_about_the_club('Барса', 'Испания', 'Сине-гранатовые', date(1899,11, 29)))
print(my_club.get_coaching_staff('Арнау Бланко'))
print()


scout_departament = Scouting_departament(
    new_player='Мохамед Салах',
    name_club='Барселона',
    president='Жоан Лапорта',
    head_coach='Ханс-Дитер Флик',
    budget=800_000_000,
    team='barcelona_squad.txt',
    name_stadion='Камп Ноу'
)
print(scout_departament.get_transfer_request(100_000_000))
print(scout_departament.get_transfer_decision())




