
int motor1_in1Pin = 6;
int motor1_in2Pin = 7;

int motor2_in1Pin = 5;
int motor2_in2Pin = 4;
 
void setup()
{
  //on initialise les pins du moteur 1
  pinMode(motor1_in1Pin, OUTPUT);
  pinMode(motor1_in2Pin, OUTPUT);
 
  //on initialise les pins du moteur 2
  pinMode(motor2_in1Pin, OUTPUT);
  pinMode(motor2_in2Pin, OUTPUT);
 
}
 
void loop()
{
 
  SetMotor2(false);
  SetMotor1(false);
 
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