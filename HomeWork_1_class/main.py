class Vehicle:
    '''Обычный класс транспортного средства'''

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage


    def get_vehicle_type(self, number_of_wheels):
        '''Метод для определения типа транспортного средства'''

        if number_of_wheels == 2:
            return f"Это мотоцикл марки {self.name}!"
        elif number_of_wheels == 3:
            return f"Это трицикл марки {self.name}!"
        elif number_of_wheels == 4:
            return f"Это автомобиль марки {self.name}!"
        else:
            return f"Я не знаю таких транспортных средств"


    def get_vehicle_advice(self):
        '''Метод определяет состояние транспортного средства'''
        try:
            if self.mileage < 50_000:
                return f"Неплохо, {self.name} можно брать!"
            elif 50_001 <= self.mileage < 100_000:
                return f"{self.name} нужно внимательно проверить!"
            elif 100_001 <= self.mileage <= 150_000:
                return f"{self.name} нужно провести полную диагностику!"
            elif self.mileage > 150_000:
                return f"{self.name} лучше не покупать"
        except TypeError:
            return f"Ошибка! Вам нужно ввести число! "




bicycle = Vehicle('Suzuki', 10000)
print(bicycle.get_vehicle_type(2))
print(bicycle.get_vehicle_advice())
print()

tricycle = Vehicle('Saab', 51_001)
print(tricycle.get_vehicle_type(3))
print(tricycle.get_vehicle_advice())
print()

auto = Vehicle('BMW', 120_000)
print(auto.get_vehicle_type(4))
print(auto.get_vehicle_advice())
print()


name = input("Введите марку транспортного средства: ")
mileage = int(input("Введите пробег у транспортного средства: "))
num_wheels = int(input("Введите кол-во колёс у транспортного средства "))

vehicle_1 = Vehicle(name, mileage)
print(vehicle_1.get_vehicle_type(num_wheels))
print(vehicle_1.get_vehicle_advice())
