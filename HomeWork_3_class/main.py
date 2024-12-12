class PowerUnit:
    '''Модель блока питания'''

    def __init__(self, power):
        self.power = power

    def get_apply_voltage(self, voltage):
        '''Метод подаёт напряжение'''
        return f"Подано напряжение: {voltage}\n"

    def __str__(self):
        return (f"Блок питания: {self.power}")

class Motherboard:
    '''Модель материнской платы'''

    def __init__(self, chipset):
        self.chipset = chipset

    def redistribute_the_voltage(self):
        return f"Напряжение перераспределено от блока питания по компонентам\n"

    def __str__(self):
        return (f"Чипсет: {self.chipset}")

class CentralProcessor:
    '''Модель центрального процессора'''

    def __init__(self, clock_frequency, number_of_cores):
        self.clock_frequency = clock_frequency
        self.number_of_cores = number_of_cores


    def activate_turbo_mode(self, activate=False):
        if activate:
            return f"Турбо режим активирован\n"
        else:
            return f"Турбо режим не активирован\n"

    def __str__(self):
        return (f"Тактовая частота: {self.clock_frequency}\n"
                f"Кол-во ядер: {self.number_of_cores}")


class AccessMemory:
    '''Модель оперативной памяти'''

    def __init__(self, memory_capacity, memory_frequency):
        self.memory_capacity = memory_capacity
        self.memory_frequency = memory_frequency

    def download_data(self):
        return f"Данные загружены\n"

    def upload_the_data(self):
        return f"Данные выгружены"

    def __str__(self):
        return (f"Объем памяти: {self.memory_capacity}\n"
                f"Частота памяти: {self.memory_frequency}")


class SsdDrive:
    '''Модель жесткого диска'''

    def __init__(self, number_of_memory):
        self.number_of_memory = number_of_memory

    def get_save_data(self):
        return f"Данные сохранены"

    def get_delete_data(self):
        return f"Данные удалены\n"

    def __str__(self):
        return f"Объём SSD накопителя: {self.number_of_memory}"

class VideoCard:
    '''Модель видеокарты'''

    def __init__(self, model, memory):
        self.model = model
        self.memory = memory

    def show_picture(self):
        return f"Картинка показана"

    def __str__(self):
        return (f"Модель видеокарты: {self.model}\n"
                f"Объём памяти: {self.memory}\n")


class PersonalComputer(PowerUnit, Motherboard, CentralProcessor, AccessMemory, SsdDrive, VideoCard):
    '''Модель персонального компьютера'''

    def __init__(self, power, chipset, clock_frequency, number_of_cores, memory_capacity, memory_frequency, number_of_memory, model, memory):
        PowerUnit.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CentralProcessor.__init__(self, clock_frequency, number_of_cores)
        AccessMemory.__init__(self, memory_capacity, memory_frequency)
        SsdDrive.__init__(self, number_of_memory)
        VideoCard.__init__(self, model, memory)

    def __str__(self):
        return (f"Блок питания: {self.power}\n"
                f"{self.get_apply_voltage(12)}\n"
                f"Чипсет: {self.chipset}\n"
                f"{self.redistribute_the_voltage()}\n"
                f"Тактовая частота: {self.clock_frequency}\n"
                f"Кол-во ядер: {self.number_of_cores}\n"
                f"{self.activate_turbo_mode(True)}\n\n"
                f"Объем памяти: {self.memory_capacity}\n"
                f"Частота памяти: {self.memory_frequency}\n"
                f"{self.upload_the_data()}\n"
                f"{self.download_data()}\n"
                f"Объём жесткого диска: {self.number_of_memory}\n"
                f"{self.get_save_data()}\n"
                f"{self.get_delete_data()}\n"
                f"Модель видеокарты: {self.model}\n"
                f"Объём видеокарты: {self.memory}\n"
                f"{self.show_picture()}"
                )


pc = PersonalComputer('750 Вт',
                      'AMD-X',
                      '2.5 ГГц',
                      6,
                      '16 ГБ',
                      '3200 МГц',
                      '512 ГБ',
                      'GeForce RTX 3060',
                      '12 ГБ')
print(pc)













