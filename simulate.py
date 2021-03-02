import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")

#BackLeg Variables
BackLegAmplitude = numpy.pi/4
BackLegFrequency = 10
BackLegPhaseOffset = 0

#Front leg variables
FrontLegAmplitude = numpy.pi/4
FrontLegFrequency = 10
FrontLegPhaseOffset = 1

#Initialize Vectors
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

#Vector to store values sinusioudally over the ranges -pi to pi
#targetAngles =(numpy.pi/4) *  numpy.sin( numpy.linspace( -numpy.pi, numpy.pi , 1000))
BackLegTargetAngles =BackLegAmplitude * numpy.sin(BackLegFrequency *  numpy.linspace( -numpy.pi, numpy.pi , 1000) + BackLegPhaseOffset)
FrontLegTargetAngles =FrontLegAmplitude * numpy.sin(FrontLegFrequency *  numpy.linspace( -numpy.pi, numpy.pi , 1000) + FrontLegPhaseOffset)
 
#print(targetAngles)

#Save targetAnles values to disk
#numpy.save('data/targetAngles.npy',targetAngles)
#exit()
numpy.save('data/BackLegTargetAngles.npy', BackLegTargetAngles)
numpy.save('data/FrontLegTargetAngles.npy', FrontLegTargetAngles)


for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	#Setting up Motor
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robot,
	jointName = "Torso_BackLeg",
	controlMode = p.POSITION_CONTROL,
	targetPosition =  BackLegTargetAngles[i] ,
	maxForce = 40)


	#2nd motor
	pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = FrontLegTargetAngles[i] ,
	maxForce = 40)




	time.sleep(1/60)

#numpy.save('data/sensorValues.npy',backLegSensorValues)
#numpy.save('data/frontSensorValues.npy',frontLegSensorValues)



print(frontLegSensorValues)
p.disconnect() 

