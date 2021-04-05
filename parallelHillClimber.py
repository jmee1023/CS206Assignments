from solution import SOLUTION
import constants as c
import copy
import os

class PARRALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")


        self.nextAvailableID = 0
        self.parents = {}
        self.count = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    #
    def Evolve(self):

        self.Evaluate(self.parents)

    #     self.parent.Evaluate("GUI")
    #
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()

        self.Evaluate(self.children)
        self.Print()
        self.Select()




    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1




    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()


    def Select(self):

        for key in self.parents:
            if(self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = self.children[key]


    def Print(self):
        print(" ")
        for key in self.parents:
            print(" ")
            print("Fitness Levels: " + str(self.parents[key].fitness) + " " + str(self.children[key].fitness))
            print(" ")
        print(" ")


    def Show_Best(self):
        lowestFitnessValue = 10
        lowestFitnessIndex = 0

        for key in self.parents:
            if self.parents[key].fitness < lowestFitnessValue:
                lowestFitnessValue = self.parents[key].fitness
                lowestFitnessIndex = key



        print("LOWESTFITNESS " + str(self.parents[lowestFitnessIndex].fitness))
        print("lowest Fitness Index " + str(lowestFitnessIndex))


        self.parents[lowestFitnessIndex].Start_Simulation("GUI")


    def Evaluate(self, solutions):
        for t in range(len(solutions)):
            solutions[t].Start_Simulation("DIRECT")



        for j in range(len(solutions)):
            solutions[j].Wait_For_Simulation_To_End()

