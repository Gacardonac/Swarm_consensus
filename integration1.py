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
​
​
class Drone(object):
    '''Drone
​
    State of drones is `orinetation`
    '''
​
    def __init__(self, identifier, initial_state, neighbors=None, time_step=0.01):
        '''Constructor
        '''
        self.identifier = identifier
        self.initial_state = initial_state
        self.current_state = self.initial_state
        self.trajectory = [self.initial_state]
        self.neighbors = neighbors
        self.time_step = time_step
        self.formation = []
​
    def move(self):
        '''
        '''
        u = self.compute_controls()
        self.current_state = self.current_state + u
        self.trajectory.append(self.current_state)
​
    def get_neighbors(self):
        '''
        '''
        return self.neighbors
​
    def get_neighbor_relative_position(self, other_drone):
        '''
        '''
        return other_drone.current_state - self.current_state
​
    def get_formation_relative_position(self, other_drone):
        '''
        '''
        for k, neighbor in enumerate(self.neighbors):
            if other_drone.identifier == neighbor.identifier:
                return self.formation[k]
​
    def compute_controls(self):
        '''
        Agent i:
        u = \sum_{j in N_i} (x_{ij} - r_{ij})
        '''
        command = 0.0
        for j in self.get_neighbors():
            command += (self.get_neighbor_relative_position(j)
                        - self.get_formation_relative_position(j))
        return command * self.time_step
​
if __name__ == '__main__':
​
    np.random.seed(1) # set seed for the random number generator
​
    T = 10 # simulation time in seconds
    dt = 0.1 # time step
    number_steps = int(round(T / dt))
​
    N = 9 # number of drones
    # initial positions of the drones
    initial_states = np.random.uniform(0, 1, size=(N, 2))
    # drone instances
    drones = [Drone(identifier, init_state, time_step=dt)
              for identifier, init_state in enumerate(initial_states)]
​
    # set neighbors for all drones
    drones[0].neighbors = [drones[1], drones[3]] # drone 0
    drones[1].neighbors = [drones[0], drones[2], drones[3], drones[4]] # drone 1
    drones[2].neighbors = [drones[1]] # drone 2
    drones[3].neighbors = [drones[0], drones[1]] # drone 3
    drones[4].neighbors = [drones[1], drones[5], drones[6], drones[8]] # drone 4
    drones[5].neighbors = [drones[4]] # drone 5
    drones[6].neighbors = [drones[4], drones[7]] # drone 6
    drones[7].neighbors = [drones[6], drones[8]] # drone 7
    drones[8].neighbors = [drones[4], drones[7]] # drone 8
​
    drones[0].formation = [np.array([1,0]), np.array([0, 1])] # r_01, r_03
    drones[1].formation = [np.array([-1, 0]), np.array([1, 0]), np.array([-1, 1]), np.array([0, 1])]# r_10, r_12, r_13, r_14
    drones[2].formation = [np.array([-1, 0])]
    drones[3].formation = [np.array([0, -1]), np.array([1, -1])]
    drones[4].formation = [np.array([0, -1]), np.array([1, 0]), np.array([-1, 1]), np.array([1, 1])]
    drones[5].formation = [np.array([-1, 0])]
    drones[6].formation = [np.array([1, -1]), np.array([1, -0])]
    drones[7].formation = [np.array([-1, 0]), np.array([1, 0])]
    drones[8].formation = [np.array([-1, -1]), np.array([-1, 0])]
    
    # simulate moving in the environment
    for k in range(number_steps):
        for d in drones:
            d.move()
​
   for k in range(number_steps)
    x1, y1 = zip(*drones[0].trajectory[k])
    f1 = client.moveToPositionAsync(x1, y1, -10, 5, vehicle_name="Drone1")
    x2, y2 = zip(*drones[1].trajectory[k])
    f2 = client.moveToPositionAsync(x2, y2, -10, 5, vehicle_name="Drone2")
    x3, y3 = zip(*drones[2].trajectory[k])
    f3 = client.moveToPositionAsync(x3, y3, -10, 5, vehicle_name="Drone3")
    x4, y4 = zip(*drones[3].trajectory[k])
    f4 = client.moveToPositionAsync(x4, y4, -10, 5, vehicle_name="Drone4")
    x5, y5 = zip(*drones[4].trajectory[k])
    f5 = client.moveToPositionAsync(x5, y5, -10, 5, vehicle_name="Drone5")
    x6, y6 = zip(*drones[5].trajectory[k])
    f6 = client.moveToPositionAsync(x6, y6, -10, 5, vehicle_name="Drone6")
    x7, y7 = zip(*drones[6].trajectory[k])
    f7 = client.moveToPositionAsync(x7, y7, -10, 5, vehicle_name="Drone7")
    x8, y8 = zip(*drones[7].trajectory[k])
    f8 = client.moveToPositionAsync(x8, y8, -10, 5, vehicle_name="Drone8")
    x9, y9 = zip(*drones[8].trajectory[k])
    f9 = client.moveToPositionAsync(x9, y9, -10, 5, vehicle_name="Drone9")
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
