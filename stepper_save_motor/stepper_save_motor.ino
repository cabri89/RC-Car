int UP = '0';
int BACK = '1';
int LEFT = '2';
int RIGHT = '3';
int incomingByte = '0';
int actualDir = '0';

int motor1_in1Pin = 6;
int motor1_in2Pin = 7;

int motor2_in1Pin = 5;
int motor2_in2Pin = 4;

void setup() {
  Serial.begin(115200);
  //on initialise les pins du moteur 1
  pinMode(motor1_in1Pin, OUTPUT);
  pinMode(motor1_in2Pin, OUTPUT);

  //on initialise les pins du moteur 2
  pinMode(motor2_in1Pin, OUTPUT);
  pinMode(motor2_in2Pin, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    actualDir = Serial.read();
  }
  goTo(actualDir);
}

void goTo(int dir){
  if(dir == UP){
    SetMotor2(true);
    SetMotor1(true);
  }else if(dir == BACK){
    SetMotor2(false);
    SetMotor1(false);
  }else if(dir == LEFT){
    SetMotor2(true);
    SetMotor1(false);
  }else if(dir == RIGHT){
    SetMotor2(false);
    SetMotor1(true);
  }
}

//Fonction qui set le moteur1
void SetMotor1(boolean reverse)
{
  digitalWrite(motor1_in1Pin, ! reverse);
  digitalWrite(motor1_in2Pin, reverse);
}

//Fonction qui set le moteur2
void SetMotor2(boolean reverse)
{
  digitalWrite(motor2_in1Pin, ! reverse);
  digitalWrite(motor2_in2Pin, reverse);
}
