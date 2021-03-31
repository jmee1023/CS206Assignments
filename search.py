import os
from hillclimber import HILL_CLIMBER

#iterations = 5

#for i in range(iterations):
    #os.system("python3 generate.py")
    #os.system("python3 simulate.py")


hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()

