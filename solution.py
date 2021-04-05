import numpy
import pyrosim.pyrosim as pyrosim
import random
import constants
import os
import time

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(2,3)


        self.weights = self.weights * 2 -1
        #rint(self.weights)


    # def Evaluate(self,runType):
    #     self.Create_World()
    #     self.Create_Body()
    #     self.Create_Brain()
    #
    #     #os.system('python3 simulate.py ' + runType)
    #     os.system("python3 simulate.py " + runType + " " + str(self.myID))
    #     #os.system("python3 simulate.py " + runType + " 0")
    #
    #     f = open("fitness" + str(self.myID) + ".txt", "r")
    #     while not os.path.exists("fitness" + str(self.myID) + ".txt"):
    #         time.sleep(0.01)
    #     value = f.read()
    #     self.fitness = float(value)
    #     print(self.fitness)

    def Start_Simulation(self, runType):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python3 simulate.py " + runType + " " + str(self.myID) + " &")
        # os.system("python3 simulate.py " + runType + " 0")

    def Wait_For_Simulation_To_End(self):

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        value = f.read()
        self.fitness = float(value)

        #print(self.fitness)

        f.close()
        os.system("rm fitness" + str(self.myID) + ".txt")


    def Create_World(self):
            pyrosim.Start_SDF("world.sdf")
            pyrosim.Send_Cube(name="Box", pos=[10, 0, .5], size=[length, width, height])
            pyrosim.End()

    # def Create_Robot():

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="0.5 0 1.0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position="1.5 0 1.0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) +".nndf")


        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # nested for loop iterating over three sensor neurons and two motor neuarons
        currentRow = 0
        currentColumn = 0
        for currentColumn in range(3):
            for currentRow in range(2):
                pyrosim.Send_Synapse(sourceNeuronName= currentColumn, targetNeuronName= currentRow+3, weight=self.weights[currentRow][currentColumn])


        pyrosim.End()

    def Mutate(self):
        randomColumn = random.randint(0,2)
        randomRow = random.randint(0,1)

        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self,nextAvailableId):
        self.myID = nextAvailableId





length = 1
width = 1
height = 1

