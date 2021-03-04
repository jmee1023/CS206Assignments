import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random
import constants as c

class SENSOR:
	def __init__(self,name):
		self.linkName = name
		self.values = numpy.zeros(c.vectorLength)
		#print(self.values)

	def Get_Value(self,t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		if(t == 999):
			print(self.values)


	def Save_Values(self):
		numpy.save('data/sensorValuesRef.npy',self.values)

