#!/usr/bin/env python
#Lars Backer

import sys
from random import randrange
from PyQt4 import QtGui, QtCore

class FlagColor(QtGui.QColor):
    def __init_(self):
        super(FlagColor,self).__init__()
	
    def getColor():
        return randrange(self.setRed(0,255)),randrange(self.setGreen(0,255)),randrange(self.setBlue(0,255))
	

def main():
    app = QApplication(sys.argv)
    flagcolor = FlagColor()
    flagcolor.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
