int S1 = HIGH;
int S2 = HIGH;
int S3 = HIGH;
int S4 = HIGH;

void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);

  Serial.begin(250000);
}

void button(int &sw, int pin, String message){
  int s1 = digitalRead(pin);
  if(sw == HIGH  && s1 == LOW){
    Serial.println(message);
    sw = LOW;
  }else{
    sw = s1;
  }
}

void loop() {
  button(S1, 2, "0");
  button(S2, 3, "1");
  button(S3, 4, "2");
  button(S4, 5, "3");

}
