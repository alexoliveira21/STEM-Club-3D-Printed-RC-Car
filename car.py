from SunFounder_PCA9685 import Servo


class Car():

    def __init__(self):
        self.defaultMotorAngle = 90
        self.defaultSteeringAngle = 100
        self.steeringPin = 0
        self.motorPin = 1
        self.steering, self.motor =self.setupServos(self.steeringPin, self.motorPin)
        self.currentSpeed = 90
        self.currentAngle = 100

    def setupServos(self, steeringPin, motorPin):
        steering = Servo.Servo(steeringPin)
        motor = Servo.Servo(motorPin)

        Servo.Servo(steeringPin).setup()
        Servo.Servo(motorPin).setup()

        steering.write(self.defaultSteeringAngle)
        motor.write(self.defaultMotorAngle)
        return steering, motor

    def updateMovement(self, motorAngle, servoAngle):
        self.steering.write(servoAngle)
        self.motor.write(motorAngle)
        self.currentAngle = servoAngle
        self.currentSpeed = motorAngle

    def emergencyStop(self):
        self.motor.write(self.defaultMotorAngle)
        self.steering.write(self.defaultSteeringAngle)
        self.currentAngle = self.defaultSteeringAngle
        self.currentSpeed = self.defaultMotorAngle
