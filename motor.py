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

class MOTOR:
	def __init__(self,jointName):
		self.jointName = jointName
		self.Prepare_To_Act()

	def Prepare_To_Act(self):
		self.amplitude = c.BlAmplitude
		self.frequency = c.BlFreq
		self.offset = c.BlOffset
		self.motors = {}
		if(self.jointName == "Torso_BackLeg"):
			self.frequency = c.BlFreq/2
		self.motorValues = self.amplitude * numpy.sin(self.frequency *  numpy.linspace( -numpy.pi, numpy.pi , c.vectorLength) + self.offset)
		#self.motorValues = self.amplitude * numpy.sin(self.frequency *  numpy.linspace( -numpy.pi, numpy.pi , c.vectorLength) + self.offset)
		print(self.jointName)
		#FrontLegTargetAngles =FrontLegAmplitude * numpy.sin(FrontLegFrequency *  numpy.linspace( -numpy.pi, numpy.pi , c.vectorLength) + FrontLegPhaseOffset)


	def Set_Value(self,robot,t):
		#Setting up Motor
		pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = self.jointName,
		controlMode = p.POSITION_CONTROL,
		targetPosition =  self.motorValues[t] ,
		maxForce = c.maxForce)	

	def Save_Values(self):
		numpy.save('data/motorValues.npy',self.motorValues)

