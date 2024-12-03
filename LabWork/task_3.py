class Pet:
    '''Модель домашнего животного'''

    def __init__(self, pet_name):
        self.__pet_name = pet_name

    def __str__(self):
        return f"Это домашнее животное, его зовут: {self.__pet_name}"

    def get_pet_name(self):
        return self.__pet_name


class Dog(Pet):
    '''Модель собаки'''
    def __init__(self, pet_name, sound, type):
        super().__init__(pet_name)
        self.sound = sound
        self.__type = type

    def get_pet_sound(self):
        return self.sound

    def get_show_name(self):
        return super().get_pet_name()

    def get_type_pet(self):
        return self.__type

    def __str__(self):
        return (f"Имя домашнего животного: {super().get_pet_name()}\n"
                f"{super().get_pet_name()} издаёт звук: {self.sound}\n"
                f"Порода: {self.__type}\n")


class Cat(Pet):
    '''Модель кота'''
    def __init__(self, pet_name, sound, type):
        super().__init__(pet_name)
        self.sound = sound
        self.__type = type

    def get_pet_sound(self):
        return self.sound

    def get_show_name(self):
        return super().get_pet_name()

    def get_type_pet(self):
        return self.__type

    def __str__(self):
        return (f"Имя домашнего животного: {super().get_pet_name()}\n"
                f"{super().get_pet_name()} издаёт звук: {self.sound}\n"
                f"Порода: {self.__type}\n")

class Parrot(Pet):
    '''Модель попугая'''

    def __init__(self, pet_name, sound, type):
        super().__init__(pet_name)
        self.sound = sound
        self.__type = type

    def get_pet_sound(self):
        return self.sound

    def get_show_name(self):
        return super().get_pet_name()

    def get_type_pet(self):
        return self.__type

    def __str__(self):
        return (f"Имя домашнего животного: {super().get_pet_name()}\n"
                f"{super().get_pet_name()} издаёт звук: {self.sound}\n"
                f"Порода: {self.__type}\n")


class Hamster(Pet):
    '''Модель Хомяка'''
    def __init__(self, pet_name, sound, type):
        super().__init__(pet_name)
        self.sound = sound
        self.__type = type

    def get_pet_sound(self):
        return self.sound

    def get_show_name(self):
        return super().get_pet_name()

    def get_type_pet(self):
        return self.__type

    def __str__(self):
        return (f"Имя домашнего животного: {super().get_pet_name()}\n"
                f"{super().get_pet_name()} издаёт звук: {self.sound}\n"
                f"Порода: {self.__type}\n")


dog = Dog('Рич', 'Гав-Гав', 'Такса (Охотник на лис)')
print(dog)

cat = Cat('Ася', 'Мяу-Мяу', 'Мейн-кун')
print(cat)

parrot = Parrot('Ара', 'Чирикает', 'Красный Ара')
print(parrot)

hamster = Hamster('Рыжик', 'Пиу', 'Обыкновенный хомяк')
print(hamster)