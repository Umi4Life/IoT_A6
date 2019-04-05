#define BUFFERSIZE 255
const int green = 2;
const int red = 3;
const int blue = 4;
const int ldr = A0;

void setup() {
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(ldr, INPUT);
  Serial.begin(9600);
//  detect();
}

void detect(int i){
  digitalWrite(i, HIGH);
  delay(1000);
  Serial.println(analogRead(ldr));
  delay(1000);
  digitalWrite(i, LOW);
}

void loop() {
  char buffer[BUFFERSIZE];
  if(Serial.available()){//there is a byte here.
    int nbytes = Serial.readBytesUntil('\n', buffer, BUFFERSIZE-1);
    buffer[nbytes] = 0; //null terminated string
    String message = String(buffer);

    if(message=="red"){
      detect(red);
    }
    if(message=="blue"){
      detect(blue);
    }
    if(message=="green"){
      detect(green);
    }
  }
}
