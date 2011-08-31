# P - power
# U - temp up
# D - temp down
# R - fanspeed up
# L - fanspeed down
# C - cool

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

def max(on):
    arduino = connect()
    if arduino:
        if not on: command(arduino, 'P')
        success = 1
    else: success = 0
    print "Max is complete."
    return success

def max2(AC):
    arduino = connect()
    if arduino:
        if not on: command(arduino, 'P')

        print "Temperature:"
        for t in range(89, 60, -1): command(arduino, 'D')
        for t in range(60, AC.temperature+1): command(arduino, 'U')
        print "Fan speed:"
        for t in range(2, 1, -1): command(arduino, 'L')
        for t in range(1, AC.fanSpeed+1): command(arduino, 'R')  
        print "power: " + str(AC.isOn)
        print "cool: on"

        success = 1
    else: success = 0

    print "Max2 is complete."
    return success

def command(robot, cmd):
    try:    
        robot.write(cmd)    
        print "sent %s to the robot" % (cmd,)
    except:    
        print "Failed to send: %s" % (cmd,)
