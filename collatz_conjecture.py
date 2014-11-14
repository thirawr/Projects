#!/usr/bin/env python
# Calculates how many steps it takes to solve the Collatz Conjecture
# @thirawr
import sys

def Stepper(n): #Recursion is nice
	if(n == 1):
		return 0
	elif(n%2 == 0):
		return 1+Stepper(n/2)
	else:
		return 1+Stepper((n*3)+1)

def Series(lower, upper): #Wrapper function for series calculation
	for i in range(lower, upper):
		print "It took %s steps for %s to reach 1." %(Stepper(i), i)

def quit():
	print "Another clean finish!"
	sys.exit()

def main(argv):
	print "Collatz Conjecture"
	print "This program computes how many steps are required to complete the Collatz sequence for any given N."

	while True:

		print "Compute sequence for a (s)eries or (i)ndividual number? "
		choice = raw_input().lower()
		while((choice != 's') and (choice != 'i')):
			print "Invalid input. Enter \'s\' for series computation or \'i\' for individual computation: "
			choice = raw_input().lower()

		if(choice == 's'):
			print "Enter positive lower bound (Negative to quit): ",
			lower = int(raw_input())
			print "Enter positive upper bound (Negative to quit): ",
			upper = int(raw_input())
			if((lower <= 0) or (upper < 0)): #Crash protection
				quit()
			Series(lower, upper)
		else:
			print "Enter N (Negative to quit): ",
			n = int(raw_input())
			if(n <= 0): #Crash protection
				quit()
			print "It took %s steps for %s to reach 1." % (Stepper(n), n)

if(__name__ == "__main__"):
	main(sys.argv)
