import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random
import constants as c


from world import WORLD
from robot import ROBOT

class SIMULATION:
	def __init__(self):
		
		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT()

	def Run(self):
		for t in range(1000):
			#print(t)
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Act(t)
			#backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
			#frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
			
			#Setting up Motor
			#pyrosim.Set_Motor_For_Joint(
			#bodyIndex = robot,
			#jointName = "Torso_BackLeg",
			#controlMode = p.POSITION_CONTROL,
			#targetPosition =  BackLegTargetAngles[i] ,
			#maxForce = c.maxForce)


			time.sleep(1/60)

	def __del__(self):
		p.disconnect()
			




	
