char msg = ' '; // for incoming serial data

void setup() {
    Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
    pinMode(13, OUTPUT);     
}

void loop() {
    // send data only when you receive data:
    if (Serial.available() > 0) {
        msg = Serial.read();
        if (msg == 'Y') {
            digitalWrite(13, HIGH);
            Serial.println("Arduino says LED on");
            delay(1000);
        }
        else if (msg == 'N') {
            digitalWrite(13, LOW);
            Serial.println("Arduino says LED off");
        }
        else Serial.println(msg);
    }
}
