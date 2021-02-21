import matplotlib.pyplot
import numpy


backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontSensorValues.npy')

matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 8)
#matplotlib.pyplot.legend("Back Leg Value")
matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")


#print(frontLegSensorValues)
#print(backLegSensorValues)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
