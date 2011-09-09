# P - power
# U - temp up
# D - temp down
# R - fanspeed up
# L - fanspeed down
# C - cool

def connect():
    import serial
    # add more locations here
    locations= ['/dev/ttyACM0', '/dev/tty.usbmodemfd141', '/dev/tty.usbserial-A700dYwR']
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
        if not checkOn(arduino): command(arduino, 'P') # turn it on if it isn't already

# would be smarter to have a function on the arduino for
# "set to minimum temperature" and "set minimum fan speed"
        print "Temperature:"
        for t in range(89, 60, -1): command(arduino, 'D') # bring it down to 60 degrees
        for t in range(60, AC.temperature+1): command(arduino, 'U') # bring it up to desired temp
        print "Fan speed:"
        for t in range(2, 1, -1): command(arduino, 'L') # bring it down to lo speed
        for t in range(1, AC.fanSpeed+1): command(arduino, 'R')  # bring it up to desired speed
        print "power: " + str(AC.isOn)
        if not AC.isOn: command(arduino, 'P') # turn it off if they want it off
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

# this won't work because I think it will just hang on readline()
# but we need something like this
def checkOn(robot):
    command(robot, 'D')
    x = robot.readline()
    return True if x else False
