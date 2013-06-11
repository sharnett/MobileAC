import serial
from time import sleep
from os import environ

class TempSensor:
    def __init__(self):
        device = '/dev/' + environ['DEVICE']
        self.connection = serial.Serial(device, 9600)
        sleep(2)
    def read(self):
        return self.command('t')
    def command(self, c):
        self.connection.write(c)
        try:
            return self.connection.readline()
        except:
            return 'failed'

if __name__ == '__main__':
    x = raw_input('q to quit: ')
    t = TempSensor()
    while x != 'q':
        print t.command(x)
        x = raw_input('q to quit: ')
