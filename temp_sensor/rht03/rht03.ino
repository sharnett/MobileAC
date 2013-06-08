static const int sensor = 8;
static int timing_pos = 0;
static int timings[64];

static int readBit(void)
{
  int usec;
  
  usec = pulseIn(sensor, HIGH);
  timings[timing_pos++] = usec;
  
  if (usec <= 40)
    return 0;
    
  return 1;
}

static uint8_t readByte(void)
{
  int i;
  uint8_t rv;
  
  for (rv = 0, i = 0; i < 8; ++i) {
    rv |= readBit() << (7 - i);
  }
  
  return rv;
}

static uint16_t readWord(void)
{
  int i;
  uint16_t rv;
  
  for (rv = 0, i = 0; i < 16; ++i) {
    rv |= readBit() << (15 - i);
  }
  
  return rv;
}

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  uint16_t temp, humidity;
  uint8_t chksum, chksum_test;
  char buf[128];
  int i;
  
  timing_pos = 0;
  pinMode(sensor, OUTPUT);
  digitalWrite(sensor, HIGH);

  delay(5000);

  digitalWrite(sensor, LOW);
  delay(18);
  digitalWrite(sensor, HIGH);
    
  pinMode(sensor, INPUT);
    
  pulseIn(sensor, LOW);
  while (digitalRead(sensor) == HIGH)
    ;
      
  humidity = readWord();
  temp = readWord();
  chksum = readByte();
    
  chksum_test = (humidity & 0xff00) >> 8;
  chksum_test += humidity & 0xff;
  chksum_test += (temp & 0xff00) >> 8;
  chksum_test += temp & 0xff;
 
  sprintf(buf, "RH %d.%d, T %d.%d, CHKSUM %s",
          humidity/10, humidity%10,
          temp/10, abs(temp%10),
          chksum == chksum_test? "Ok" : "Fail");
  Serial.println(buf);
  /*
  Serial.println("Timings.\n");
    
  for (i = 0; i < 16; ++i) {
    sprintf(buf, "%d. %d", i, timings[i]);
    Serial.println(buf);
  }
  */
}
