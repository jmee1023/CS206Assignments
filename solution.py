import numpy
import pyrosim.pyrosim as pyrosim
import random
import constants as c
import os
import time

class SOLUTION:
    def __init__(self,nextAvailableID):

        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numMotorNuerons,c.numSensorNeurons) * 2 - 1


        self.weights = self.weights * 2 -1
        #rint(self.weights)



    def Start_Simulation(self, runType):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        #os.system("python3 simulate.py " + runType + " " + str(self.myID) + " 2&>1 &")
        os.system("python3 simulate.py " + runType + " " + str(self.myID) + " &")

        # os.system("python3 simulate.py " + runType + " 0")

    def Wait_For_Simulation_To_End(self):

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.2)
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
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="0 -0.5 1.0",jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, -0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position="0 0.5 1.0",jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position="-0.5 0 1.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position="0.5 0 1.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position="0 1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position="0 -1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position="-1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position="1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])




        pyrosim.End()



    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) +".nndf")


        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        #new
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")





        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        #new
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLowerLeg")









        # nested for loop iterating over three sensor neurons and two motor neuarons
        currentRow = 0
        currentColumn = 0
        for currentColumn in range(c.numSensorNeurons):
            for currentRow in range(c.numMotorNuerons):
                pyrosim.Send_Synapse(sourceNeuronName= currentColumn, targetNeuronName= currentRow+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])


        pyrosim.End()




    def Mutate(self):
        randomColumn = random.randint(0,c.numSensorNeurons -1)
        randomRow = random.randint(0,c.numMotorNuerons-1)

        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self,nextAvailableId):
        self.myID = nextAvailableId





length = 1
width = 1
height = 1

