#include <Servo.h>

const int servoPin = 5; 	  	//Servo Pin
const int SOFT_POT_PIN = A7;

//Variables
long duration; 		          	//Time it Took for Sound to Comeback
int distance; 				       	//Location of Ball from Sensor
int pos = 0; 				        	//Servo Position
double StartAngle = 102; 	  	//Angle of servo when beam is parallel to the ground
double pError,iError,dError; 	//Error values associated with PID
double Output; 					      //Sum of error values multiplied by their corresponding gains
double prevError; 			     	//Error from previous iteration
unsigned long prevTime,now; 	//Previous time and current time
double dt; 						        //Change in time

int Setpoint = 0;  			    	//Desired point on the beam

//Gains
float Kp = 0.16; 			       	//Proportion constant
float Ki = 0.00005; 		     	//Integral   constant
float Kd = 7; 					      //Derivative constant



Servo servo;  				       	//Create servo object to control the servo

//Initial setup
void setup() {
  servo.attach(servoPin);  		//Attaches the servo on pin 13 to the servo object
  servo.write(StartAngle); 		//Initiate the motor to the horizonal angle
  pinMode(SOFT_POT_PIN, INPUT);
  Serial.begin(9600); 			//Starts the serial communication
}
void loop() {
  float softPotAnalog = analogRead(SOFT_POT_PIN);
  float ballposition = softPotAnalog * (100 / 951.0);
  Serial.println(ballposition);
  //PID Algorithm
  now = millis();
  dt = (now - prevTime);
  pError = Setpoint - ballposition;
  dError = (pError - prevError) / dt;
  iError = iError + (pError * dt);
  if (iError > 10) {
    iError = 10;				//Error greater than 10 are ignored; noise
  }

  Output = Kp * pError + Ki * iError + Kd * dError;

  //Upper and Lower Bound of PID
  if (Output >20) {
    Output = 20;
  }
  if (Output <-20) {
    Output = -20;
  }

  servo.write(StartAngle + Output);

  //Serial output
  Serial.print("PID: ");
  Serial.println(Output);
  
  //Set previous error and time
  prevError = pError;
  prevTime = now;

}