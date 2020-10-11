class CPU:
    @staticmethod
    def freeze():
        print('freeze')

    @staticmethod
    def jump(address):
        print('jump to address \'{}\''.format(address))

    @staticmethod
    def execute():
        print('execute')


class Memory(object):
    @staticmethod
    def load(position):
        print('load data from position \'{}\''.format(position))


class HardDrive:
    @staticmethod
    def read(position):
        print('read data from position \'{}\''.format(position))


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hardDrive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        self.memory.load('boot sector')
        self.cpu.jump('boot sector')
        self.cpu.execute()
        self.hardDrive.read('boot sector')


computer = Computer()
computer.start_computer()
