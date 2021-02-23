import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")


#Initialize Vectors
backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)

for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	#Setting up Motor
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robot,
	jointName = "Torso_BackLeg",
	controlMode = p.POSITION_CONTROL,
	targetPosition =-(math.pi)/4.0 ,
	maxForce = 500)


	#2nd motor
	pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = (math.pi)/4.0 ,
	maxForce = 500)




	time.sleep(1/60)

numpy.save('data/sensorValues.npy',backLegSensorValues)
numpy.save('data/frontSensorValues.npy',frontLegSensorValues)
print(frontLegSensorValues)
p.disconnect() 

