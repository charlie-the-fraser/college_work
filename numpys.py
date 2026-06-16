import numpy 
import math 
bob = numpy.array([120, 135, 150, 98, 75, 200, 143]).astype(float)

print(numpy.mean(bob))
print(bob.sum())
print(numpy.max(bob))
print(numpy.min(bob))

bob *= 1.1
print(bob)

