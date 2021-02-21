import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)

for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

	#backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	time.sleep(1/60)

numpy.save('data/sensorValues.npy',backLegSensorValues)
numpy.save('data/frontSensorValues.npy',frontLegSensorValues)
print(frontLegSensorValues)
p.disconnect() 

