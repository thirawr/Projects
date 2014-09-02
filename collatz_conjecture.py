#!/usr/bin/env python
# Calculates how many steps it takes to solve the Collatz Conjecture
import sys

print "Collatz Conjecture"
print "This program determines how many steps are required to complete the\n\
Collatz sequence for any given N."

run = True

while run:
	print "Enter N (-1 to quit): ",
	orig = int(raw_input())
	if(orig == -1):
		run = False
		sys.exit()
	n = orig

	def Stepper(n):
		if(n == 1):
			return 0
		elif(n%2 == 0):
			return 1+Stepper(n/2)
		else:
			return 1+Stepper((n*3)+1)


	steps = Stepper(n)

	print "It took %s steps for %s to reach 1." % (steps, orig)
