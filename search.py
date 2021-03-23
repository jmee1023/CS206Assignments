import os

iterations = 5

for i in range(iterations):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")