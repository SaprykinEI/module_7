class Car:
    '''Модель Автомобиля'''

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_information_car(self):
        return (f"Автомобиль: {self.brand}\n"
                f"Модель: {self.model}\n"
                f"Год выпуска: {self.year}\n")


class Wheels(Car):
    '''Колёса автомобиля'''

    def __init__(self, brand, model, year, brand_wheels, diameter_wheels):
        super().__init__(brand, model, year)
        self.brand_wheels = brand_wheels
        self.diameter_wheels = diameter_wheels

    def get_information_car(self):
        data_car = super().get_information_car()
        return (f"{data_car}")

    def get_inform_wheels(self):
        return (f"Бренд колёс: {self.brand_wheels}\n "
                f"Диаметр колёс: {self.diameter_wheels}\n")


class Engine(Car, Wheels):
    '''Модель двигателя'''

    def __init__(self, brand, model, year, brand_wheels, diameter_wheels, model_engine, engine_power):
        super().__init__(brand, model, year, brand_wheels, diameter_wheels)
        self.model_engine = model_engine
        self.engine_power = engine_power

    def get_information_car(self):
        data_car = super().get_information_car()
        return (f"{data_car}")

    def get_inform_wheels(self):
        data_wheels = super().get_inform_wheels()
        return data_wheels

    def get_inform_engine(self):
        return (f"Модель двигателя: {self.model_engine}\n"
                f"Мощность двигателя: {self.engine_power}\n")
#
#
#
car_bmw = Car('BMW', 'X5-M', '2022')
print(car_bmw.get_information_car())

car_bmw = Wheels('BMW', 'X5-M', 2022, 'Michelin', 24)
print(car_bmw.get_inform_wheels())

car_bmw = Engine('BMW', 'X5-M', 2022, 'Michelin', 24, 'B57D30 ', '286 л.с')
print(car_bmw.get_information_car())
print(car_bmw.get_inform_engine())
print(car_bmw.get_inform_engine())


