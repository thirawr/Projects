#!/usr/bin/env python
# This program calculates pi to a specified decimal place.
import math

pi = math.pi
places = -1

while (places < 0):
	print "Enter the number of decimal places to calculate pi: ",
	places = raw_input()

print "Printing %s decimal places of pi:" %places
print "%.(places)f" % pi