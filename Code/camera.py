from picamera import PiCamera
import time
import numpy as np

rgb_text = ['Red', 'Green', 'Blue']  # array for naming color


class Camera:
    def __init__(self):
        # picamera setup
        h = 640  # change this to anything < 2592 (anything over 2000 will likely get a memory error when plotting
        cam_res = (int(h), int(0.75 * h))  # keeping the natural 3/4 resolution of the camera
        cam_res = (int(16*np.floor(cam_res[1]/16)), int(32*np.floor(cam_res[0]/32)))
        self.cam = PiCamera()

        # making sure the picamera doesn't change white balance or exposure
        # this will help create consistent images
        self.cam.resolution = (cam_res[1], cam_res[0])
        self.cam.framerate = 30
        time.sleep(2) #let the camera settle
        self.cam.iso = 100
        self.cam.shutter_speed = self.cam.exposure_speed
        self.cam.exposure_mode = 'off'
        gain_set = self.cam.awb_gains
        self.cam.awb_mode = 'off'
        self.cam.awb_gains = gain_set

        # prepping for analysis and recording background noise
        # the objects should be removed while background noise is calibrated
        self.data = np.empty((cam_res[0], cam_res[1],3), dtype=np.uint8)
        self.noise = np.empty((cam_res[0], cam_res[1],3), dtype=np.uint8)
        x,y = np.meshgrid(np.arange(np.shape(self.data)[1]), np.arange(0, np.shape(self.data)[0]))

        #input("press enter to capture background noise (remove colors)")
        self.cam.capture(self.noise,'rgb')
        self.noise = self.noise-np.mean(self.noise) # background 'noise'

    def sees_blue(self):
        self.cam.capture(self.data,'rgb')
        mean_array = []
        for ii in range(0,3): 
            # calculate mean and STDev
            mean_array.append(np.mean(self.data[:,:,ii]-np.mean(self.data)-np.mean(self.noise[:,:,ii])))
            #std_array.append(np.std(data[:,:,ii]-np.mean(data)-np.mean(noise[:,:,ii]))) 
            #print('-------------------------') 
            #print(rgb_text[ii]+'---mean: {0:2.1f}, stdev: {1:2.1f}'.format(mean_array[ii],std_array[ii]))

        # guess the color of the object 
        print('The Object is: {}'.format(rgb_text[np.argmax(mean_array)])) 
        print('--------------------------')
        time.sleep(1)
        # if the color of the object is blue, then stop
        return np.argmax(mean_array) == 2







'''
camera = PiCamera()
   
camera.start_preview()
time.sleep(2)
camera.capture('/home/pi/Desktop/jj.jpg')
camera.stop_preview()
'''