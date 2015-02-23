#!/usr/bin/env python
#Richards Zheng

from flag_color import *

class Country():
		# Create the class country
		def __init__(self, country):
			self.country = country
		
		# Return the string given in the terminal
		def __str__(self):
			return "Hello from {}".format(self.country)

		
