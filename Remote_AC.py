def connect():
    import serial
    locations= ['/dev/tty.usbserial-A700dYwR']
    for device in locations:    
        try:    
            print "Trying...",device  
            robot = serial.Serial(device, 9600)   
            print "connected"
            break  
        except:    
            print "Failed to connect on",device    
            robot = False
    return robot

def max(status):
    arduino = connect()
    if arduino: on(arduino) if status else off(arduino)
    return "Max is complete.\n"

def max2(AC):
    arduino = connect()
    off(arduino)

    print "Temperature:"
    for t in range(89, 60, -1):
        blink(arduino, .1) 
        print t
    for t in range(60, AC.temperature+1):
        blink(arduino, .2) 
        print t
    print "Fan speed:"
    for t in range(2, 1, -1):
        blink(arduino, .5) 
        print t
    for t in range(1, AC.fanSpeed+1):
        blink(arduino, .5) 
        print t
    print "power: " + str(AC.isOn)
    on(arduino) if AC.isOn else off(arduino)
    print "cool: on"
    return "Max2 is complete.\n"

def on(robot):
    try:    
        robot.write('Y')    
        print 'On!'
#        print robot.readline().rstrip()  
    except:    
        print "Failed to send!"   

def off(robot):
    try:    
        robot.write('N')    
        print 'Off!'
#        print robot.readline().rstrip()  
    except:    
        print "Failed to send!"   

def blink(robot, pause):
    from time import sleep
    on(robot)
    sleep(pause)
    off(robot)
