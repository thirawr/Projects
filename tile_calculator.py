#!/usr/bin/env python
# Calculates the total cost of tile for a room, given cost, width and height
# @thirawr
import sys

def price_calc(w, h, c): #Width, height, cost
	if((w <= 0) or (h <= 0)):
		print "Width or height is less than or equal to 0"
	elif(c < 0):
		print "Negative cost"
	return((w*h)*c)

def main(argv):
	print "Enter floor width: ",
	width = float(raw_input())
	print "Enter floor height: ",
	height = float(raw_input())
	print "Enter tile cost: ",
	cost = float(raw_input())
	print "Buying %s units^2 of tile would cost $%s." %(width*height, price_calc(width, height, cost))

if(__name__ == "__main__"):
	main(sys.argv)