import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random
import constants as c
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
	def __init__(self):

		self.robot = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()
		self.motors = {}
	

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)


	def Sense(self,t):
		for i in self.sensors:
			#self.values[t] = self.sensors[i].Get_Value()
			self.sensors[i].Get_Value(t)
		
