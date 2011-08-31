def max(status):
    import serial  
    import time  

    locations=[
    '/dev/tty.usbserial-A700dYwR',
    '/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',  
    '/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']    

    for device in locations:    
        try:    
            print "Trying...",device  
            arduino = serial.Serial(device, 9600)   
            break  
        except:    
            print "Failed to connect on",device     

    loop = 1
    while loop:
        command = 'On' if status else 'Off'
        if command == 'On':
            try:    
                arduino.write('Y')    
                time.sleep(1)  
                print arduino.readline()  
                print 'On!'
            except:    
                print "Failed to send!"   
            loop = 0
        elif command == 'Off':
            try:    
                arduino.write('N')    
                time.sleep(1)  
                print arduino.readline()  
                print 'Off!'
            except:    
                print "Failed to send!"
            loop = 0
        elif command == 'end' or command == 'End' or command == 'END':
            print "End!"
            loop = 0
        else:
            print('Command does not compute.')
    return "Max is complete."
