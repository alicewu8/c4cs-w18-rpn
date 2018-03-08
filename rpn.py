#!/usr/bin/env python3

# rpn calculators are easier to use because they have a stack
# eg 1 1 + is equal to 1 + 1, 1 1 + 2 * is equal to (1+1) * 2

# a dictionary is a hash table

# operator is a library of operators
import operator
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

# create a hash table that maps from a hash table to a function
# writing a dictionary (key : value)
operators = {
# defining add and subtract like they are functions
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
# added another comma after truediv because it's specified for how you
# should write Python and makes for cleaner commits
		'/': operator.truediv,
		'^': operator.pow,
	}

def calculate(arg):
# data type is list: a default constructor
# list is an object that has default behavior
# lists behave list stacks; can append and pop and push
	stack = list()

# range-based for loop: setting value for each token
# arg.split() takes the string and turns it into tokens
	for token in arg.split(): 
		try:
	value = int(token)
	 stack.append(value)

# if anything in the try block fails, program jumps to except block
	 except ValueError:
# returns the corresponding operator according to the dictionary
# definition
	 function = operators[token]
# pop these arguments from the stack
	arg2 = stack.pop()
	arg1 = stack.pop()
	result = function(arg1, arg2)
	stack.append(result)
logging.debug(stack)


	if len(stack) != 1:
	raise TypeError

# empty the stack and add a return value
return stack.pop()

	def summation(arg):
# initializes an empty list
		stack = list()

# stores the numbers from the argument into the list
	for num in arg.split():
		try:
	value = int(token)
	 stack.append(value)

	 for value in stack:
	summation += value
stack.append(summation)

return stack.pop()

	def main():
		while True:
		print(calculate(input('rpn calc> ')))

		if __name__ == '__main__':
main()
