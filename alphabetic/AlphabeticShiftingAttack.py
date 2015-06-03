'''
Created on 10 sept. 2013

@author: miistair
'''

from PyQt4.QtCore import QObject, pyqtSlot, pyqtSignal

class AlphabeticShiftingAttack(QObject):
    
    textDecyphered = pyqtSignal(object) 
    def __init__(self):
        '''
        Constructor
        '''
        QObject.__init__(self)
        self.asciiOffset = 0
        self.decypheredText = ''
        self.cypheredText = ''
        
    @pyqtSlot()
    def setCypheredText(self):
        self.cypheredText = self.sender().toPlainText()
        self.decypher()
        
    def decypher(self):
        clearText = ''
        for c in self.cypheredText:
            if c is not '\t' and c is not '\r' and c is not ' ' and c is not '\n':
                clearText += chr((ord(c) + self.asciiOffset) % 255)
            else:
                clearText += c
        self.textDecyphered.emit(clearText)
        
    
    @pyqtSlot(int)
    def setAsciiOffset(self,offset):
        self.asciiOffset = offset
        self.decypher()
    
        
