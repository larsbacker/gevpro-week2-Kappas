#!/usr/bin/python3
#Richards Zheng
import sys
from country import country

# function to read the file and return a list 
# of the objects created through the country class
def readnames(stdin):
	countries = []
	for line in sys.stdin:
		country1 = country(line)
		countries.append(country1)
	return(countries)
	
			
readnames(sys.argv)
