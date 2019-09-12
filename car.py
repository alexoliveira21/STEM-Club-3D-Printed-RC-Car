from SunFounder_PCA9685 import Servo

# this class creates a Car object which is used to initialize all the motor servo and steering servo on the
# physical car. default motor and steering angles differ based on which motor and servo you use so it is highly
# recomended you test them before running this code. If you are using different pins on your PWM board make sure
# to change it in this car class


class Car():

    # creates the car object with all the required default values
    def __init__(self):
        self.defaultMotorAngle = 90
        self.defaultSteeringAngle = 100
        self.steeringPin = 0
        self.motorPin = 1
        # create Servo objects for motor and steering
        self.steering, self.motor =self.setupServos(self.steeringPin, self.motorPin)

        #these values hold the current speed and angle of the vehicle for training purposes
        self.currentSpeed = 90
        self.currentAngle = 100

    # setup Servo objects using the Servo class from the SunFounder_PCA9685 folder
    def setupServos(self, steeringPin, motorPin):
        steering = Servo.Servo(steeringPin)
        motor = Servo.Servo(motorPin)

        Servo.Servo(steeringPin).setup()
        Servo.Servo(motorPin).setup()

        # writes (or sets) the default speed and angles to the servos
        steering.write(self.defaultSteeringAngle)
        motor.write(self.defaultMotorAngle)

        return steering, motor

    # changes speed and/or steering of the servos
    def updateMovement(self, motorAngle, servoAngle):
        #write the speed and angle to the servos
        self.steering.write(servoAngle)
        self.motor.write(motorAngle)

        #update the speed and angle values
        self.currentAngle = servoAngle
        self.currentSpeed = motorAngle

    # performs an "emergency stop" by setting the angles to the default values
    def emergencyStop(self):
        self.motor.write(self.defaultMotorAngle)
        self.steering.write(self.defaultSteeringAngle)
        self.currentAngle = self.defaultSteeringAngle
        self.currentSpeed = self.defaultMotorAngle
