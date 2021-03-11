import matplotlib.pyplot
import numpy

#TESTTTTT

# Load in Values From files
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontSensorValues.npy')
targetAngles = numpy.load('data/targetAngles.npy')

FrontLegTargetAngles = numpy.load('data/FrontLegTargetAngles.npy')
BackLegTargetAngles = numpy.load('data/BackLegTargetAngles.npy')


#Plot data 
#matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 8)
#matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")
#matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.plot(FrontLegTargetAngles, label = "Front Leg Motor")
matplotlib.pyplot.plot(BackLegTargetAngles, label = "Back Leg Motor")




matplotlib.pyplot.legend()
matplotlib.pyplot.show()
