import setup_path
import airsim
import numpy as np
import os
import tempfile
import pprint
import cv2
from PIL import Image
from array import array
import time
import random
from random import seed
from random import randint

client = airsim.MultirotorClient()
client.confirmConnection()

client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.enableApiControl(True, "Drone3")
client.enableApiControl(True, "Drone4")
client.enableApiControl(True, "Drone5")
client.enableApiControl(True, "Drone6")
client.enableApiControl(True, "Drone7")
client.enableApiControl(True, "Drone8")
client.enableApiControl(True, "Drone9")
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")
client.armDisarm(True, "Drone3")
client.armDisarm(True, "Drone4")
client.armDisarm(True, "Drone5")
client.armDisarm(True, "Drone6")
client.armDisarm(True, "Drone7")
client.armDisarm(True, "Drone8")
client.armDisarm(True, "Drone9")


# airsim.wait_key('Press any key to takeoff')
# client.takeoffAsync().join()
airsim.wait_key('Press any key to takeoff')
f1 = client.takeoffAsync(vehicle_name="Drone1")
f2 = client.takeoffAsync(vehicle_name="Drone2")
f3 = client.takeoffAsync(vehicle_name="Drone3")
f4 = client.takeoffAsync(vehicle_name="Drone4")
f5 = client.takeoffAsync(vehicle_name="Drone5")
f6 = client.takeoffAsync(vehicle_name="Drone6")
f7 = client.takeoffAsync(vehicle_name="Drone7")
f8 = client.takeoffAsync(vehicle_name="Drone8")
f9 = client.takeoffAsync(vehicle_name="Drone9")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()
f7.join()
f8.join()
f9.join()

#random number generation for the duration of the rotations
seed(1)

#client.rotateByYawRateAsync(20,1).join()
airsim.wait_key('Press any key to rotate')
f1 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone1")
f2 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone2")
f3 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone3")
f4 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone4")
f5 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone5")
f6 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone6")
f7 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone7")
f8 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone8")
f9 = client.rotateByYawRateAsync(20, randint(0, 20), vehicle_name="Drone9")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()
f7.join()
f8.join()
f9.join()

client.armDisarm(False, "Drone1")
client.armDisarm(False, "Drone2")
client.armDisarm(False, "Drone3")
client.armDisarm(False, "Drone4")
client.armDisarm(False, "Drone5")
client.armDisarm(False, "Drone6")
client.armDisarm(False, "Drone7")
client.armDisarm(False, "Drone8")
client.armDisarm(False, "Drone9")
client.reset()

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False, "Drone1")
client.enableApiControl(False, "Drone2")
client.enableApiControl(False, "Drone3")
client.enableApiControl(False, "Drone4")
client.enableApiControl(False, "Drone5")
client.enableApiControl(False, "Drone6")
client.enableApiControl(False, "Drone7")
client.enableApiControl(False, "Drone8")
client.enableApiControl(False, "Drone9")


