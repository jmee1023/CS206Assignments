import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5
for count in range(5):
	length = 1
	width = 1
	height = 1
	y = 0
	x+=1
	z = 0
	pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
	for count1 in range(5):
		length = 1
		width = 1
		height = 1
		z = 0
		y +=1
		pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
		for count3 in range(5):
			z +=1
			#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
			length *= .9
			width *= .9
			height *= .9		
			pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[x,y+1,z+1] , size=[length,width,height])
pyrosim.End()

