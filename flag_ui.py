#!/usr/bin/env python
#Cock
import sys
from PyQt4 import QtGui, QtCore
from country import Country
from flag_color import *

def readnames(stdin):
    countries = []
    countries1 = []
    for line in sys.stdin:
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
        self.lbl = QtGui.QLabel("0", self)
        self.lbl.move(450, 90)        
        self.combo1 = QtGui.QComboBox(self)
        self.combo1.move(50, 50)
        self.rino = QtGui.QFrame(self)
        self.colourzz = QtGui.QColor(0,0,0)
        self.rino.setStyleSheet("Qframe { background-color: %s}" % self.colourzz.name())
        # Use the function to get the currencies and fill the
        # Comboboxes with currencies (Euro/Dollars/Peso etc)
        # Also sorts the lists
        hallo = readnames(self)
        self.combo1.addItems(sorted(list(hallo)))
        self.combo1.currentIndexChanged.connect(self.on1Activated)

        # Set window size and draw
        self.setGeometry(700, 700, 700, 200)
        self.rino.setGeometry(400, 400, 400, 200)
        self.setWindowTitle('Currency converter')
        self.show()
        
    def on1Activated(self, box1):
		result = self.combo1.currentText()
		self.lbl.setText(str(result))
		self.lbl.adjustSize()		
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
