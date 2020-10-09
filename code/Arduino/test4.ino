
#include <Servo.h>   
Servo servo;
Servo servo1;     //用于内部旋转
int servoPin = 9;
int servo1Pin = 10;
int trigPin = 6;    
int echoPin = 7;   
long duration, distance;   
long aver[3];   
char temp;
int singal = 0;

void setup() {     
  servo.attach(servoPin); 
  servo1.attach(servo1Pin); 
  pinMode(trigPin, OUTPUT);  
  pinMode(echoPin, INPUT); 
  servo.write(0); 
  delay(1000);
  servo.detach();
  Serial.begin(9600);
  servo1.write(90); 
} 

void measure() {  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(15);
  digitalWrite(trigPin, LOW);
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  distance = duration *0.034 / 2;
}

void loop() {
  for (int i=0;i<=2;i++) {   
    measure();               
    aver[i]=distance;            
    delay(50);           
  }
  distance=(aver[0]+aver[1]+aver[2])/3; 
  if (distance<40) {   
    servo.attach(servoPin);
    delay(1);
    servo.write(90);   
  }
  if(singal == 1){  
    servo.write(0);
    delay(1000);    
    servo.detach();
    singal = 0;
  } 
  //while(Serial.available() == 0){}
  if(Serial.available()){
    temp = Serial.read();
    if(temp == '2'){
      servo1.write(180);
      delay(1000);
      servo1.write(90);
      singal = 1;
     }
    if(temp == '1'){
      servo1.write(0);
      delay(1000);
      servo1.write(90);
      singal = 1;
     }
  }
}
