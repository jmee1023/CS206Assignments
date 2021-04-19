import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random


#Back Leg Variables
BlAmplitude = numpy.pi/4
BlFreq = 10
BlOffset = 0

#Front leg variables
FlAmplitude = numpy.pi/4
FlFreq = 10
FlOffset = 1

#Initialize Vectors
vectorLength = 1000
#MAX force
maxForce = 100

numberOfGenerations = 15

populationSize = 10

numSensorNeurons = 9
numMotorNuerons = 8

motorJointRange = 0.2

