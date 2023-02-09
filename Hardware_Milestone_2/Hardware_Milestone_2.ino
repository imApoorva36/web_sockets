int latchPin = D1;//RCLK
int clockPin = D2;//SRCLK
int dataPin = D3;//SER

void setup() {
  pinMode(latchPin, OUTPUT);//Initialising the latchpin pin as output
  pinMode(clockPin, OUTPUT);//Initialising the clockpin pin as output
  pinMode(dataPin, OUTPUT);//Initialising the datapin pin as output
}

void loop() {
    digitalWrite(latchPin, LOW);//putting it initially as low
    shiftOut(dataPin, clockPin, MSBFIRST,B10000000 );//here the binary code referred to that particular output pin of the register where we want the pin to connect to the led to glow
    digitalWrite(latchPin, HIGH);
    delay(1000);//waiting for 1 second
    digitalWrite(latchPin, LOW);// again putting it as low for going to high again later, in which case high means that the led goes
    shiftOut(dataPin, clockPin, MSBFIRST,B00001100 );
    digitalWrite(latchPin, HIGH);
    delay(1000);//waiting for 1 second
    digitalWrite(latchPin, LOW);// again putting it as low for going to high
    shiftOut(dataPin, clockPin, MSBFIRST,B00110000 );
    digitalWrite(latchPin, HIGH);
    delay(1000);//waiting for 1 second
    digitalWrite(latchPin, LOW);// again putting it as low for going to high
    shiftOut(dataPin, clockPin, MSBFIRST,B01000000 );
    digitalWrite(latchPin, HIGH);
    delay(1000);//waiting for 1 second
    ESP.reset();//resetting the register for the fresh next input that can be easily taken
}