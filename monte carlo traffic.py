# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:26:58 2016

@author: anthonyweston
"""

# Adaptation of the Nagel-Schrekenberg traffic model
# Import numpy for use of a 2-d array and random number generator

import numpy as np
import matplotlib.pyplot as plt
import time

#creates the roadway array, each row represents a spot along the road and each column is a lane
#one car can exist at a time at one array index
roadway = np.empty([1001, 4], dtype=object)
avg_vel = np.zeros([1001,1])
instances = np.zeros([1001,1])

#class for each car in the model
# two values v for velocity and r for random probability of slowing down at each step

class Car:
    def __init__(self, v, r):
        self.v = v
        self.r = r

        
# adds the new cars into the model at the first poisiton in the array
# parameter t determines the threshold for creating a new car
# each car starts with speed 1 and a slowing probability of a random number between 1 and 0

def add(t):
    
    a = np.random.rand(4,1)
    
    for x in range(4):
        if a[x] >= t:
            roadway[0,x] = Car(1, np.random.random())
            

#increases the speed of the car by one unit at each timestep
def faster(a):
    if a.v < 20:
        a.v += 1
    
#once all the speed changes have taken place this function moves the car forward according to its speed
def move(a,x,y):
    #if it will exceed the length of the road after its move, the car is deleted from the model
    if a.v + x > 1000:
        roadway[x,y] = None
    #otherwise the car moves forward by a.v spaces where v is the car's speed
    else:
        roadway[x + a.v, y] = a
        # if the speed is positive and non-zero (the car moves forward) it deletes the car from its previous location
        # if the car has no speed(it stays in the same place) the car does not get deleted
        # the car cannot have speed zero
        if a.v > 0:
            roadway[x,y] = None

#checks the area in front of the car to make sure it will not occupy the same spot as another car
def checkdistance(a,x,y):
    #checks the spots in the range up to the speed of the car, because this is the space it will move in and a car cannot hop over another car
    for spot in range(1,a.v+1):
        #make sure that we are not checking outside of the array (results in an error)
        if spot + x < 1000:
            # check to see if there is an instance of the car object(another car) in the given spot
            if isinstance(roadway[x+spot], Car) == True:
                #slow down the car so that it will move into the spot directly behind the next car
                a.v = spot - 1
                break   

# slows down the car with probability r of occurance (member variable of car object)
def slow(a,t):
    # the objects property r represents an individual driver, and this value is unique driver to simulate real conditions 
    chance = a.r * np.random.random()
    #default value of t is 0.25 (random numbers with standard distribution in range 0 to 1)
    # average value is 0.5 so threshold is 0.5^2
    #if the random product exceeds the threshold the speed of the car decreases by 1
    if chance > t:
        a.v -= 1
      

#engine runs each of the functions, in their specific order at each timestep
def engine(a,x,y):
    faster(a)
    checkdistance(a,x,y)
    #this is where the threshold for slowing down is set
    slow(a, 0.25)
    move(a,x,y)
        
        
def main(t,timesteps):
    print("Model in Progress...")
    # runs for the number of timesteps defined by the user
    for timestep in range(0,timesteps):
        #add cars at the start of the model domain
        add(t)
        #loop through the roadway array
        for cols in range(0,4):
            #moves from the end of the road backwards so cars do not overlap because the one behind moves first
            for rows in range(1000, -1, -1):
                if isinstance(roadway[rows, cols], Car) == True:
                    
                    #cumulative_results[rows,cols] += 1;
                    a = roadway[rows, cols]
                    engine(a, rows, cols)
                    avg_vel[rows] += a.v
                    instances[rows] += 1
                     
            

print("Welcome to the Monte Carlo Traffic Model")
t = float(input("Enter a car creation threshold between 0 and 1: "))
# fix this loop (only goes once)
if t < 0 or t > 1:
    while t < 0 or t > 1:
        t = float(input("Invalid entry, please enter a new threshold value between 0 and 1: "))
times = int(input("Enter the number of timesteps you would like to have: "))



start_time = time.time()
main(t,times)
print("Model Completed. Running Time: %s seconds" % (str(time.time() - start_time)))


result = np.divide(avg_vel, instances)

plt.plot(result)
plt.ylabel("Speed (units)")
plt.xlabel("Distance")
plt.title("Monte Carlo Traffic Model Average Speed")

