import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random
import constants as c
from simulation import SIMULATION



simulation = SIMULATION()
simulation.Run()


#BackLeg Variables
#BackLegAmplitude = c.BlAmplitude
#BackLegFrequency = c.BlFreq
#BackLegPhaseOffset = c.BlOffset

#Front leg variables
#FrontLegAmplitude = c.FlAmplitude
#FrontLegFrequency = c.FlFreq
#FrontLegPhaseOffset = c.FlOffset

#Initialize Vectors
#backLegSensorValues = numpy.zeros(c.vectorLength)
#frontLegSensorValues = numpy.zeros(c.vectorLength)

#Vector to store values sinusioudally over the ranges -pi to pi
#BackLegTargetAngles =BackLegAmplitude * numpy.sin(BackLegFrequency *  numpy.linspace( -numpy.pi, numpy.pi , c.vectorLength) + BackLegPhaseOffset)
#FrontLegTargetAngles =FrontLegAmplitude * numpy.sin(FrontLegFrequency *  numpy.linspace( -numpy.pi, numpy.pi , c.vectorLength) + FrontLegPhaseOffset)
 
#print(targetAngles)

#Save targetAnles values to disk
#numpy.save('data/targetAngles.npy',targetAngles)
#exit()
#numpy.save('data/BackLegTargetAngles.npy', BackLegTargetAngles)
#numpy.save('data/FrontLegTargetAngles.npy', FrontLegTargetAngles)


#for i in range(1000):
	#p.stepSimulation()
	#backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	#frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	#Setting up Motor
	#pyrosim.Set_Motor_For_Joint(
	#bodyIndex = robot,
	#jointName = "Torso_BackLeg",
	#controlMode = p.POSITION_CONTROL,
	#targetPosition =  BackLegTargetAngles[i] ,
	#maxForce = c.maxForce)


	#2nd motor
	#pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robot,
        #jointName = "Torso_FrontLeg",
        #controlMode = p.POSITION_CONTROL,
        #targetPosition = FrontLegTargetAngles[i] ,
	#maxForce = c.maxForce)




	#time.sleep(1/60)

#numpy.save('data/sensorValues.npy',backLegSensorValues)
#numpy.save('data/frontSensorValues.npy',frontLegSensorValues)



#print(frontLegSensorValues)
#p.disconnect() 

