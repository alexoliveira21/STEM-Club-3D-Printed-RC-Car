# This file is the main file of the project that pieces together everything. Here we host the server
# for the website that will be used to control the car. We first create our car and initialize all the
# required variables we also initialize the cars camera. functions provided will allow for control of
# the vehicle via server. Running this code will start a server which you will be able to change the cars
# movement

from flask import Flask, render_template, request
from flask_cors import CORS
from carCamera import CarCamera
from car import Car
import time
import pandas as pd
import os

# the paths for where the csv and video files will be saved.
csv_path = "/home/pi/Downloads/CAR/csvFiles"
video_path = "/home/pi/Downloads/CAR/videos"

# dictionary that holds the recorded speeds, angles and their respective times
speed_angle_data = {'Time':[], 'Speed':[], 'Angle':[], 'Start Time': 0, 'Stop Time' : 0}

#creates the car and  camera objects
car = Car()
camera = CarCamera(video_path)

#creates the Flask app which allows us to host our control site
app = Flask(__name__)
CORS(app)

# adds data to the dictionary
def appendToList(currentTime, speed, steering):
    speed_angle_data['Time'].append(currentTime)
    speed_angle_data['Speed'].append(speed)
    speed_angle_data['Angle'].append(steering)

# resets the dictionary to be empty
def resetList():
    speed_angle_data = {'Time':[], 'Speed':[], 'Angle':[], 'Start Time': 0, 'Stop Time' : 0}


# home page of the site which just initializes the html file
@app.route('/')
def carSite():
    return render_template('carControl.html', message = "Ready to Drive!")

# function that will stop the car and the camera and will save the data in a csv file
@app.route('/stop', methods= ['GET', 'POST'])
def stop():
    #stop the car
    car.emergencyStop()

    #record stop time
    speed_angle_data['Stop Time'] = camera.stop()
    print("Car and Recording Stopped")

    #create a dataframe using Pandas to save data as a csv file
    df = pd.DataFrame(speed_angle_data)

    #save csv to specified path
    df.to_csv('{0}{1:f}'.format(csv_path, speed_angle_data['Start Time']))

    #resets the dictionary to be able to record and save new data if the recording restarts
    resetList()

    return "Stopped"

#start the camera recording
@app.route('/record_data', methods=['GET', 'POST'])
def record_data():

    # starts the video recording and records the start time
    speed_angle_data['Start Time'] = camera.start()
    print("Now Recording")

    return "Recording"

# responds to changes in the speed buttons pressed via the server
@app.route('/change_speed', methods= ['GET', 'POST'])
def change_speed():

    #save the time where speed was changed
    currentTime = time.time()

    #request speed and angle data from the site
    speed = request.args.get('speed', 90)
    steering = request.args.get('steering', 100)

    # update the cars speed
    car.updateMovement(int(speed), int(steering))

    # add updated data to the dictionary
    appendToList(currentTime, speed, steering)

    print('Speed: {}    Steering: {}    Time: {}'.format(speed, steering, currentTime))

    return "Speed changed"

# responds to interactions from the steering slider on the server site
@app.route('/data_update', methods= ['GET', 'POST'])
def data_update():

    #save the current time when angle was changed
    currentTime = time.time()

    #request speed and angle data from the site
    speed = request.args.get('speed', 90)
    steering = request.args.get('steering', 90)

    # update the car's steering angle
    car.updateMovement(int(speed), int(steering))

    # add updated data to the dictionary
    appendToList(currentTime, speed, steering)

    print('Speed: {0}    Steering: {1}     Time: {2:f}'.format(speed, steering, currentTime))

    return "Data Updated"

# initializes the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = False)
