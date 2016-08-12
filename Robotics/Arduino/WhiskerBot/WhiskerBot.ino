# include <Servo.h>
Servo servoRight;
Servo servoLeft;
Servo sensorLeft;
Servo sensorRight;
int leftPin = 5;
int rightPin = 7;
int pin = 4;

int note_E4 = 329.6;

long whole_note = 1600; // change tempo by changing duration of one measure
long half_note = whole_note / 2;
long quarter_note = whole_note / 4;

int song[1][2] = {{note_E4, quarter_note}};

void setup() {
  // put your setup code here, to run once:
servoLeft.attach(12);
servoRight.attach(13);
servoRight.writeMicroseconds(1500);
servoLeft.writeMicroseconds(1500);
pinMode(leftPin, INPUT);
pinMode(rightPin, INPUT);
pinMode(pin, OUTPUT);
}

void r_forward(int forward){
  servoRight.writeMicroseconds(forward);

}
void l_forward(int value){
    servoLeft.writeMicroseconds(value);
}
void r_back(int hi) {
  servoRight.writeMicroseconds(hi);
}
void l_back(int dog) {
  servoLeft.writeMicroseconds(dog);
}

void tone(int song[1][2]){
  int i = 0;
  for (i; i < 1; i++) {
    tone(pin, song[i][0]);
    delay(song[i][1]); 
}
}
void loop() {
  // put your main code here, to run repeatedly:
if (digitalRead(leftPin) == 0) {
  tone(song);
  l_back(1600);
  r_back(1400);
  delay(500); 
  l_forward(1500);
  r_forward(1500);
  l_forward(1700);
  delay(500);
}

else if (digitalRead(rightPin) == 0) {
  tone(song);
  l_back(1400);
  r_back(1600);
  delay(500); 
  l_forward(1500);
  r_forward(1500);
  r_forward(1300);
  delay(500);
}

else if ((digitalRead(rightPin) == 0) && (digitalRead(leftPin) == 0)) {
  tone(song);
  l_back(1400);
  r_back(1600);
  delay(500); 
  l_forward(1500);
  r_forward(1500);
  r_forward(1700);
  delay(500);
}
else {
  l_forward(1700);
  r_forward(1300);
}


}
