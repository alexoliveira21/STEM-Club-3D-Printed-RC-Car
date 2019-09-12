from picamera import PiCamera
import time
import os

class CarCamera():

    def __init__(self, path):
        self.camera = PiCamera()
        self.camera.resolution = ('720p')
        self.camera.framerate = 24
        self.path = path

    def start(self):
        os.chdir(path)
        start_time = (time.time())
        self.camera.start_recording("{0:f}".format(start_time), format = 'h264')
        return float(time.time())


    def stop(self):
        if(self.camera.recording):
            self.camera.stop_recording()
            return float(time.time())
