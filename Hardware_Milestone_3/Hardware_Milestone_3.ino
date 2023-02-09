int latchPin = D1;//RCLK
int clockPin = D2;//SRCLK
int dataPin = D3;//SER

void setup() {
  pinMode(latchPin, OUTPUT);//Initialising the latchpin pin as output
  pinMode(clockPin, OUTPUT);//Initialising the clockpin pin as output
  pinMode(dataPin, OUTPUT);//Initialising the datapin pin as output
}

void loop() {
    //delay(1000);
    digitalWrite(latchPin, LOW);//Putting it as low for going to high again later, in which case high means that the led goes
    shiftOut(dataPin, clockPin, MSBFIRST,B11100100 );//here the binary code referred to that particular output pin of the register where we want the pin to connect to the led to glow
    digitalWrite(latchPin, HIGH);
    delay(10);//waiting for a small interval of time so that the next execution is done without any error or miscommunicationbtwn register and nodemcuv1.0
}