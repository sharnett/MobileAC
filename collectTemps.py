# r - get temp/hum reading

import sqlite3
import re
from time import sleep
from datetime import datetime

def connect():
    import serial
    # add more locations here
    locations= ['/dev/tty.usbmodemfd141', '/dev/tty.usbserial-A700dYwR']
    for device in locations:    
        try:    
            print "Trying...",device  
            robot = serial.Serial(device, 9600, timeout=2.00)   
            print "connected"
            break  
        except:    
            print "Failed to connect on",device    
            robot = False
    return robot

def command(robot, cmd):
    try:    
        robot.write(cmd)    
    except:    
        print "failed to send command"
    line = robot.readline().strip()
    if line:
        m = re.search(r'(\d+\.\d+)\s+(\d+\.\d+)', line)
        result = [.1*round(10*float(m.group(1))), float(m.group(2))]
    else: 
        print "failed to read line"
        result = 0
    return result


def insertReading(conn, curs, t, h):
    curs.execute('''select count(id) from mobileAC_thermoreading''')
    n = curs.fetchone()[0]
    dt =  datetime.now()
    dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    print "adding %s %2.1f %2.1f to database" % (dt, t, h)
    curs.execute('''insert into mobileAC_thermoreading values (?, 1, ?, ?, ?)''', (n+1, dt, t, h))
    conn.commit()

arduino = connect()
db = sqlite3.connect('db.db')
c = db.cursor()
for i in range(4*10): 
    result = command(arduino, 'r')
    if result:
        insertReading(db, c, result[0], result[1])
    sleep(900)
