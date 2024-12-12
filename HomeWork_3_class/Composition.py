from main import PowerUnit, Motherboard, CentralProcessor, AccessMemory, SsdDrive, VideoCard

class PComputer:
    '''Модель Компьютера выполненная с помощью композиции'''

    def __init__(self, power_unit: object = PowerUnit, motherboard: object = Motherboard,
                 central_processor: object = CentralProcessor,
                 access_memory: object = AccessMemory, ssd_drive: object = SsdDrive,
                 videocard: object = VideoCard):
        self.power_unit = power_unit
        self.motherboard = motherboard
        self.central_processor = central_processor
        self.access_memory = access_memory
        self.ssd_drive = ssd_drive
        self.videocard = videocard


power = PowerUnit('750 В')
motherboard = Motherboard('AMD-X')
processor = CentralProcessor('2.5 ГГц', 6)
access_memory = AccessMemory('16 ГБ', '3200 МГц')
ssd = SsdDrive('512 ГБ')
videocard = VideoCard('GeForce RTX 3060', '12 ГБ')

pc = PComputer(power, motherboard, processor, access_memory, ssd, videocard)

print(pc.power_unit)
print(pc.power_unit.get_apply_voltage(12))
print(pc.motherboard)
print(pc.motherboard.redistribute_the_voltage())
print(pc.central_processor)
print(pc.central_processor.activate_turbo_mode(True))
print(pc.access_memory)
print(pc.access_memory.upload_the_data())
print(pc.access_memory.download_data())
print(pc.ssd_drive)
print(pc.ssd_drive.get_save_data())
print(pc.ssd_drive.get_delete_data())
print(pc.videocard)
print(pc.videocard.show_picture())