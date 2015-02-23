#!/usr/bin/env python
#Cock
import sys
from PyQt4 import QtGui, QtCore
from country import Country
from flag_color import FlagColor
from random import randrange


def readnames(stdin):
    countries = []
    countries1 = []
    for line in sys.stdin:
	    if line != "/n":
		    z = line
		    country1 = Country(line)
		    countries.append(country1)
		    countries1.append(z)
    return countries1


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
		          
		# Draw QLabel and move it      
        
        # Draw Qcomboboxes 1 and 2 and move them
        self.combo1 = QtGui.QComboBox(self)
        self.combo1.move(50, 50)
        self.col = QtGui.QColor(150, 175, 90)
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(50, 90, 240, 30)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        self.col1 = QtGui.QColor(125, 133, 45)
        self.square1 = QtGui.QFrame(self)
        self.square1.setGeometry(75, 90, 240, 30)
        self.square1.setStyleSheet("QWidget { background-color: %s }" % self.col1.name())
        self.col2 = QtGui.QColor(78, 35, 49)
        self.square2 = QtGui.QFrame(self)
        self.square2.setGeometry(100, 90, 240, 30)
        self.square2.setStyleSheet("QWidget { background-color: %s }" % self.col2.name())        
        # Use the function to get the currencies and fill the
        # Comboboxes with currencies (Euro/Dollars/Peso etc)
        # Also sorts the lists
        hallo = readnames(self)
        self.combo1.addItems(sorted(list(hallo)))
        self.combo1.currentIndexChanged.connect(self.on1Activated)

        # Set window size and draw
        self.setGeometry(700, 700, 700, 200)
        self.setWindowTitle('Currency converter')
        self.show()
        

        
        
    def on1Activated(self):
        self.kappa = QtGui.QColor(150, 175, 90)
        a, b, c = FlagColor.getColor(self.kappa)
        self.col = QtGui.QColor(a, b, c)       
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
