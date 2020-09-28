# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:02:01 2020

@author: nboni
"""
import vrep
import sys
import numpy as np
#import matplotlib.pyplot as plt
import time
#import math
#import pandas as pd


    

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print("Conexion no exitosa")
    sys.exit("No se pudo conectar")
time.sleep(1)

# handlers Definition

#errorCode, target_handle =vrep.simxGetObjectHandle(clientID,'Plane',vrep.simx_opmode_oneshot_wait)
errorCode, targetDrone =vrep.simxGetObjectHandle(clientID,'Quadricopter_target',vrep.simx_opmode_oneshot_wait)
errorCode, drone_handle =vrep.simxGetObjectHandle(clientID,'Quadricopter',vrep.simx_opmode_oneshot_wait)


Target=[2,2,2]

errorCode, DronePos  =vrep.simxGetObjectPosition(clientID,drone_handle,-1,vrep.simx_opmode_blocking)
errorCode, DronePos  =vrep.simxGetObjectPosition(clientID,drone_handle,-1,vrep.simx_opmode_blocking)

    
DiffTarget=np.array(Target)-np.array(DronePos)
DistTarget=(np.linalg.norm(DiffTarget))

#errorCode=vrep.simxSetObjectPosition(clientID, targetDrone, -1, [0.01,0,1], vrep.simx_opmode_blocking)
print('Info  ')
print(DistTarget)

while (DistTarget>0.5):
    DirTarget=(DiffTarget)/(DistTarget+0.1)
    errorCode, DronePos  =vrep.simxGetObjectPosition(clientID,drone_handle,-1,vrep.simx_opmode_blocking)
    DroneFly=np.array(DronePos)+DirTarget/2
    errorCode=vrep.simxSetObjectPosition(clientID, targetDrone, -1, DroneFly, vrep.simx_opmode_blocking)
    
    print('Info  ')
    print(DirTarget)
    print(DronePos)
    time.sleep(0.01)
    errorCode, DronePos  =vrep.simxGetObjectPosition(clientID,drone_handle,-1,vrep.simx_opmode_blocking)
    DiffTarget=np.array(Target)-np.array(DronePos)
    DistTarget=(np.linalg.norm(DiffTarget))
    
    

    























"""
    errorCode,sensor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor'+str(x),vrep.simx_opmode_blocking)
    errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor_handle,vrep.simx_opmode_streaming)    



   errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor_h[x-1],vrep.simx_opmode_buffer)                
        sensor_val=np.append(sensor_val,np.linalg.norm(detectedPoint))     
        
        
    #mayor o = 9 Es lejos; entre 8.9 y 5 es medio; menor a 4.9 es cerca
    sensor_sq=sensor_val[0:4]*sensor_val[0:4] 
    prueba=[4,4,4,4]
    prueba1=sensor_val[0:4]*prueba[0:4]
    
    vlf,vrf=logica_difusa(prueba1[0],prueba1[1],prueba1[2],prueba1[3])
    
    min_ind=np.where(sensor_sq==np.min(sensor_sq))
    min_ind=min_ind[0][0]
    
    
    if sensor_sq[min_ind]<3.0:
        steer=-1/sensor_loc[min_ind]
    else:
        steer=0      
 
    
    vlff=vlf/50
    vrff=vrf/50
    
    sensor_prueba=[]
    time.sleep(0.002) 

"""


