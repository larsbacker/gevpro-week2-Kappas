#!/usr/bin/env python
#Richards Zheng


class country():
		
		# Create the class country
		def __init__(self, string):
			self.string = string
		
		# Return the string given in the terminal
		def __str__(self):
			return "Hello from {}".format(self.string)
		
		

