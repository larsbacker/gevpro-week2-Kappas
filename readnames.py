#!/usr/bin/python3
#Richards Zheng
import sys
from flag_color import *

# function to read the file and return a list 
# of the objects created through the country class
class Country():
	# Create the class country
    def __init__(self, country):
        self.country = country
        self.color = FlagColor()
    
    def returnDit(self):
        return self.country
        return self.color
