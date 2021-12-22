import os
from parallelHillClimber import PARRALLEL_HILL_CLIMBER

#iterations = 5

#for i in range(iterations):
    #os.system("python3 generate.py")
    #os.system("python3 simulate.py")


phc = PARRALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

