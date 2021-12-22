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
	def __init__(self,directOrGUI,solutionID):

		if(directOrGUI == "DIRECT"):
			self.physicsClient = p.connect(p.DIRECT)
		else:
			self.physicsClient = p.connect(p.GUI)

		self.directOrGUI = directOrGUI
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT(solutionID)
		#self.Get_Fitness()


	def Run(self):
		for t in range(1000):
			#print(t)
			p.stepSimulation()
			self.robot.Sense(t)
			self.robot.Think()
			self.robot.Act(t)
			if (self.directOrGUI == "GUI"):
				time.sleep(1 / 60)

		self.Get_Fitness()


		#if(self.directOrGUI == "GUI"):
			#time.sleep(1/60)

	def Get_Fitness(self):
		self.robot.Get_Fitness()

	def __del__(self):
		p.disconnect()
			




	
