from flask import Flask, render_template, request
from flask_cors import CORS
from carCamera import CarCamera
from car import Car
import time
import pandas as pd
import os

speed_angle_data = {'Time':[], 'Speed':[], 'Angle':[], 'Start Time': 0, 'Stop Time' : 0}

car = Car()
camera = CarCamera()

app = Flask(__name__)
CORS(app)


@app.route('/')
def carSite():
    return render_template('carControl.html', message = "Hello!")

@app.route('/stop', methods= ['GET', 'POST'])
def stop():
    car.emergencyStop()
    print("Car Stopped")
    speed_angle_data['Stop Time'] = camera.stop()
    print("Recording Stopped")

    df = pd.DataFrame(speed_angle_data)
    os.chdir("/home/pi/Downloads/CAR/csvFiles")
    df.to_csv('{0:f}'.format(speed_angle_data['Start Time']) + '.csv')
    resetList()
    return "Stopped"

@app.route('/record_data', methods=['GET', 'POST'])
def record_data():

    speed_angle_data['Start Time'] = camera.start()
    print("Now Recording")

    return "Recording"

@app.route('/change_speed', methods= ['GET', 'POST'])
def change_speed():
    currentTime = time.time()
    speed = request.args.get('speed', 90)
    steering = request.args.get('steering', 100)
    car.updateMovement(int(speed), int(steering))
    appendToList(currentTime, speed, steering)
    print('Speed: {}    Steering: {}'.format(speed, steering))
    return "Speed changed"


@app.route('/data_update', methods= ['GET', 'POST'])
def data_update():
    currentTime = time.time()
    speed = request.args.get('speed', 90)
    steering = request.args.get('steering', 90)
    appendToList(currentTime, speed, steering)
    car.updateMovement(int(speed), int(steering))
    print('Speed: {0}    Steering: {1}     Time: {2:f}'.format(speed, steering, currentTime))
    return "Data Updated"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = False)

def appendToList(currentTime, speed, steering):
    speed_angle_data['Time'].append(currentTime)
    speed_angle_data['Speed'].append(speed)
    speed_angle_data['Angle'].append(steering)

def resetList():
    speed_angle_data = {'Time':[], 'Speed':[], 'Angle':[], 'Start Time': 0, 'Stop Time' : 0}
