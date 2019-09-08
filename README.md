# autonomour-rc-car

## Goal

This was a summer project completed by the West Valley College STEM Club. Our goal was to create a 3D printed RC car which we would then train to be autonomous using Tensorflow. The design of the car was aquired from thingiverse which is linked here: https://bit.ly/2lIrMFG. We wanted to have an autonomous vehicle travel arround the West Valley campus performing certain tasks. Below is a detailed process of how we achieved this goal. We have included all the materials needed, and detailed all the necessary steps to build the car, all the required libraries and code to make sure the car will run.

## Main Materials Used:
- 3D printer (Ender 300) ~ $200
- Digital Servo for steering (https://amzn.to/2UYHtJa) ~20
- Brishless Motor (https://amzn.to/2klFfDj) ~ 30
- PCA9685 PWM Servo Driver (https://amzn.to/2konXp8) ~ $9
- 30A ESC (https://amzn.to/2lCDsKk) ~ $15
- Raspberry Pi 4: 4GB RAM (https://amzn.to/2ky3eis) ~ $80
- Any 3S Lipo battery to power motor and servo: at least 5000 mAh (https://amzn.to/2Y8qxkY) ~$30
- Any 3S Lipo battery to power Raspberry Pi: at least 2200mAh (https://amzn.to/2k4TQmf) ~$21
- Lipo Battery Charger (https://amzn.to/2OVzt9H) ~ $25
- Raspberry Pi 5 megapixel Camera (https://amzn.to/2lDEcPe) ~ $15
- Wheels (https://amzn.to/2IsWEn3) ~ $15

### Smaller parts:
- 3.5mm Bullet Connectors (https://amzn.to/2XTJt7O) ~ $8
- Male to Female Bullet Connectors Power Plugs (https://amzn.to/2LX9E61) ~ $9
- Metal Servo Horns (https://amzn.to/2Dd21TR) ~ $10
- Shocks (https://amzn.to/2UhFsmE) ~ $25
- Steering Rod End (https://amzn.to/2X1mAu6) ~ $10

## Raspberry Pi
- Flash an SD card and setup the raspian operating system 
- Update and upgrade system:
  ```
  sudo apt-get update
  sudo apt-get upgrade
  ```
- Install python basics:
  ```
  sudo apt-get install build-essential python-dev python-distlib python-setuptools python-pip python-wheel libzmq-dev libgdal-dev
  sudo apt install python3-dev python3-pip
  ```
- Enable Camera, SSH, I2C:
  ```
  sudo raspi-config
  ```
  - Scroll to interface options and enable Camera, SSH, I2C
  
### Required libraries for this project:
  - **_Numpy:_**
    ```
    sudo apt install libatlas-base-dev
    sudo pip install numpy
    ```
  - **_Pandas:_**
    ```
    sudo apt-get install python-pandas
    ```
  - **_Tensorflow (AI):_**
    ```
    sudo pip3 install tensorflow
    ```
  - **_H5PY (AI model):_**
    ```
    sudo apt-get install libhdf5-serial-dev
    sudo pip install h5py
    ```
  - **_Keras (AI):_**
    ```
    sudo pip install pillow
    sudo pip install keras
    ```
  - **_Flask and Flask-Cors (Web Server):_**
    ```
    sudo pip install flask
    sudo  pip install -U flask-cors
    ```
  - **_Picamera:_**
    ```
    sudo apt-get install python-picamera python3-picamera
    ```
  - **_Servo and PCA9685_** (included in Sunfounder_PCA9685 folder) 
  - **_OPENCV_** (Process to download below)
  
## Installing OPENCV:




  

