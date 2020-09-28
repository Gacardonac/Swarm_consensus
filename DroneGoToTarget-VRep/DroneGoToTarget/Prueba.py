# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:29:23 2020

@author: nboni
"""

import vrep
import sys
import numpy as np
import matplotlib.pyplot as plt
import time

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID!=-1:
    print ('Connected to remote API server')
else:
    print("Conexion no exitosa")
    sys.exit("No se pudo conectar")


errorCode,sensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor1',vrep.simx_opmode_blocking)

#first time
time.sleep(2)
startTime=time.time()

errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming)
errorCode,cam1_handle=vrep.simxGetObjectHandle(clientID,'Cam1',vrep.simx_opmode_blocking)
errorCode,resolution,image=vrep.simxGetVisionSensorImage(clientID,cam1_handle,0,vrep.simx_opmode_streaming)

while time.time()-startTime < 5:
        errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
        errorCode,resolution,image=vrep.simxGetVisionSensorImage(clientID,cam1_handle,0,vrep.simx_opmode_buffer)                    
        time.sleep(0.005)

errorCode,leftmotor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_blocking)
errorCode,rightmotor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_blocking)

errorCode=vrep.simxSetJointTargetVelocity(clientID,leftmotor_handle,0.2,vrep.simx_opmode_oneshot )
errorCode=vrep.simxSetJointTargetVelocity(clientID,rightmotor_handle,0.2,vrep.simx_opmode_oneshot )

imagen=np.array(image,dtype=np.uint8)
imagen.resize([resolution[0],resolution[1],3])
plt.imshow(imagen,origin='lower')