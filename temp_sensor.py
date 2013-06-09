import serial
from time import sleep

class TempSensor:
    def __init__(self):
        device = '/dev/tty.usbmodemfd121'
        self.connection = serial.Serial(device, 9600)
        sleep(2)
    def read(self):
        try:    
            self.connection.write(' ')    
            return self.connection.readline()
        except:
            return 'failed'

if __name__ == '__main__':
    x = raw_input('q to quit: ')
    t = TempSensor()
    while x != 'q':
        print t.read()
        x = raw_input('q to quit: ')
