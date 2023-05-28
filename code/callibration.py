import matplotlib.pyplot as plt
import numpy as np
import serial
import cv2
import time
from threading import Thread

def get_img(polarization_angle: int) -> np.ndarray:
    polarization_angle_to_angle = {0: 15, 45: 120, 135: 65, 90: 179}
    port.write(bytes(str(polarization_angle_to_angle[polarization_angle]), 'utf-8'));
    time.sleep(2);
    _, frame = cam.read();
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



port = serial.Serial('/dev/ttyUSB0', 9600);
cam = cv2.VideoCapture(2);
stokes_parametrs = np.loadtxt('stokes_parametrs.txt')

get_img(int(input()))
