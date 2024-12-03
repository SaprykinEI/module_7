class Wheels():
    '''Колёса автомобиля'''

    def __init__(self, brand_wheels, diameter_wheels):
        self.brand_wheels = brand_wheels
        self.diameter_wheels = diameter_wheels

    def get_information_wheels(self):
        return (f"Бренд колёс: {self.brand_wheels}\n"
                f"Диаметр колёс: {self.diameter_wheels}\n")


class Engine():
    '''Модель двигателя'''

    def __init__(self, model_engine, engine_power):
        self.model_engine = model_engine
        self.engine_power = engine_power

    def get_information_engine(self):
        return (f"Модель двигателя: {self.model_engine}\n"
                f"Мощность двигателя: {self.engine_power}\n")


class Doors():

    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors
    
    def get_information_doors(self):
        return (f"Количество дверей: {self.number_of_doors}")


class Car(Wheels, Engine, Doors):
    '''Модель Автомобиля'''

    def __init__(self, brand_wheels, diameter_wheels, model_engine, engine_power, number_of_doors, brand, model, year):
        super().__init__(brand_wheels, diameter_wheels)
        Engine.__init__(self, model_engine, engine_power)
        Doors.__init__(self, number_of_doors)
        self.brand = brand
        self.model = model
        self.year = year

    def get_information_car(self):
        return (f"Автомобиль: {self.brand}\n"
                f"Модель: {self.model}\n"
                f"Год выпуска: {self.year}\n"
                f"{super().get_information_wheels()}"
                f"{super().get_information_engine()}"
                f"{super().get_information_doors()}")


car_bmw = Car('Michelin',
              24,
              'B57D30',
              '286 л.с',
              '5',
              'BMW',
              'X5-M',
              2020)
print(car_bmw.get_information_car())




