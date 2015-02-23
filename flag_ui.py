#!/usr/bin/env python
# Lars Backer Richards Zheng

import sys
from PyQt4 import QtGui, QtCore
from readnames import *
from flag_color import *
from random import randrange

# Function to select 3 random values and return them
def numberpicker():
	return randrange(0, 255), randrange(0, 255), randrange(0, 255)

# Function to read the file in and return a list of country names
def readnames(stdin):
    countries = []
    countries1 = []
    for line in sys.stdin:
        z = line.strip()
        country1 = Country(line)
        countries.append(country1)
        countries1.append(z)
    return countries1


class Example(QtGui.QWidget):
    # Create class
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):   
        
        # Draw Qcomboboxe 1 and move it
        self.combo1 = QtGui.QComboBox(self)
        self.combo1.move(50, 50)
        
        # Draw 3 QFrames and move them
        self.col = QtGui.QColor(0, 0, 0)
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(50, 90, 240, 30)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        self.col1 = QtGui.QColor(0, 0, 0)
        self.square1 = QtGui.QFrame(self)
        self.square1.setGeometry(50, 115, 240, 30)
        self.square1.setStyleSheet("QWidget { background-color: %s }" % self.col1.name())
        self.col2 = QtGui.QColor(0, 0, 0)
        self.square2 = QtGui.QFrame(self)
        self.square2.setGeometry(50, 140, 240, 30)
        self.square2.setStyleSheet("QWidget { background-color: %s }" % self.col2.name())        
		
		# Used readnames function to return a list into countrynames variable
		# Added the list items into the QCombobox
		# Changing QCombobox index activates flagChanger function
        countrynames = readnames(self)
        self.combo1.addItems(sorted(countrynames))
        self.combo1.currentIndexChanged.connect(self.flagChanger)

        # Set window size and draw
        self.setGeometry(350, 350, 350, 200)
        self.setWindowTitle('Random Flags')
        self.show()
    
        # Change the color of the three QFrames
    def flagChanger(self):
        a, b, c = numberpicker()
        a1, b1, c1 = numberpicker()
        a2, b2, c2 = numberpicker()
        self.col = QtGui.QColor(a, b, c)
        self.col1 = QtGui.QColor(a1, b1, c1)
        self.col2 = QtGui.QColor(a2, b2, c2)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        self.square1.setStyleSheet("QWidget { background-color: %s }" % self.col1.name())
        self.square2.setStyleSheet("QWidget { background-color: %s }" % self.col2.name())
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
