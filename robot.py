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
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
	def __init__(self,solutionID):
		self.solutionID = solutionID
		self.robot = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		os.system("rm brain" + str(solutionID) + ".nndf")


		
	

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Prepare_To_Act(self):
		self.motors = {}

		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)
			


	def Sense(self,t):
		for i in self.sensors:
			#self.values[t] = self.sensors[i].Get_Value()
			self.sensors[i].Get_Value(t)
		

	def Act(self,t):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)

				desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange

				self.motors[jointName].Set_Value(self.robot,desiredAngle)




		#for i in self.motors:
				#self.motors[i].Set_Value(self.robot,desiredAngle)

	def Think(self):
		self.nn.Update()
		#self.nn.Print()

	def Get_Fitness(self):
		stateOfLinkZero = p.getLinkState(self.robot,0)
		#print(stateOfLinkZero)
		positionOfLinkZero = stateOfLinkZero[0]
		#print(positionOfLinkZero)
		xCoordinateOfLinkZero = positionOfLinkZero[0]
		#print(xCoordinateOfLinkZero)

		#f = open("fitness" + str(self.solutionID) +".txt","w")
		#f.write(str(xCoordinateOfLinkZero))

		f = open("tmp" + str(self.solutionID) + ".txt","w")
		f.write(str(xCoordinateOfLinkZero))
		f.close()
		os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")






