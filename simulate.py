import pybullet_data
import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import random
import constants as c
import sys
from simulation import SIMULATION


directOrGui = sys.argv[1]
simulation = SIMULATION(directOrGui)
simulation.Run()
simulation.Get_Fitness()





