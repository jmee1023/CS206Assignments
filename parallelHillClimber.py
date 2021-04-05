from solution import SOLUTION
import constants as c
import copy

class PARRALLEL_HILL_CLIMBER:
    def __init__(self):

        self.nextAvailableID = 0
        self.parents = {}

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    #
    def Evolve(self):
        for t in range(len(self.parents)):
            self.parents[t].Start_Simulation("DIRECT")



        for j in range(len(self.parents)):
            self.parents[j].Wait_For_Simulation_To_End()




    #     self.parent.Evaluate("GUI")
    #
    #     for currentGeneration in range(c.numberOfGenerations):
    #         self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()



    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.SetId(self.nextAvailableID)
        self.nextAvailableID +=1

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print("Fitness Levels: " + str(self.parent.fitness) + " " + str(self.child.fitness))

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass