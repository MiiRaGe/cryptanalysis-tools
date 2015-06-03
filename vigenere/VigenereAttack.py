'''
Created on 6 sept. 2013

@author: miistair
'''
from collections import deque
from PyQt4.QtCore import QObject, pyqtSlot, pyqtSignal
from vigenere.PyGenere import VigCrack
from vigenere.Coincidence import computeKeyLength

class VigenereWrap(QObject):
    '''
    classdocs
    '''

    keyWorkCracked = pyqtSignal(object)
    textDecyphered = pyqtSignal(object)

    def __init__(self):
        '''
        Constructor
        '''
        QObject.__init__(self)
        self.cypheredText = ''
        self.translationTable = ''.maketrans('éèêëàâïîùûüöôç','eeeeaaiiuuuooc')
        self.key =  'key'
        self.language = 'EN'
        self.keyLength = 1
        self.keyOffset = 0
        self.crackedKeyWord = ''
        self.displayCipheredText = False
        self.displayKey = False


    @pyqtSlot()
    def bruteForce(self):
        self.keyLength = computeKeyLength(self.cypheredText)
        if self.keyLength == -1:
            self.keyWorkCracked.emit('Key : Length not found')
        else:
            self.crackKeyWord()

    @pyqtSlot(int)
    def setKeyLength(self,length):
        self.keyLength = length
        self.crackKeyWord()

    @pyqtSlot(object)
    def setLanguage(self,lang):
        self.language = self.sender().itemText(lang)
        self.crackKeyWord()

    @pyqtSlot()
    def crackKeyWord(self):
        self.crackedKeyWord = VigCrack(self.cypheredText).set_language(self.language).crack_codeword(self.keyLength)
        self.keyWorkCracked.emit('Key : '+ self.crackedKeyWord)

    @pyqtSlot()
    def tryKey(self):
        self.setKey(self.crackedKeyWord)
        self.decypher()

    @pyqtSlot()
    def setCypheredText(self):
        self.cypheredText = self.sender().toPlainText().lower()
        self.cypheredText.translate(self.translationTable)
        self.decypher()

    @pyqtSlot()
    def decypher(self):
        self.clearText = ''
        cypheredLine = ''
        clearTextLine = ''
        self.keyString = ''
        if self.key is '' :
            self.key = 'key'
        key = deque(self.key)
        for i in range(0,self.keyOffset):
            key.append(key.popleft())
        for c in self.cypheredText:
            if c.isalpha():
                k = key.popleft()
                key.append(k)
                cypheredLine += c
                c = chr((ord(c)- ord(k))%26 + 97)
                clearTextLine += c
                self.keyString += k
            elif c is '\n' or c is '\r' or c is '':
                if self.displayCipheredText:
                    self.clearText +=  'Cyphered= ' +cypheredLine + '\n'
                if self.displayCipheredText:
                    self.clearText += 'Key     = ' + self.keyString + '\n'
                self.clearText +=  'Clear   = ' + clearTextLine +  '\n\n'
                clearTextLine = ''
                cypheredLine = ''
                self.keyString = ''
            else:
                cypheredLine += c
                clearTextLine += c
                if c is '\t':
                    self.keyString += c
                else:
                    self.keyString += ' '
        if self.displayCipheredText:
            self.clearText +=  'Cyphered= ' +cypheredLine + '\n'
        if self.displayCipheredText:
            self.clearText += 'Key     = ' + self.keyString + '\n'
        self.clearText +=  'Clear   = ' + clearTextLine +  '\n\n'
        self.textDecyphered.emit(self.clearText)


    @pyqtSlot(str)
    def setKey(self,key):
        keyTemp = ''
        for c in key:
            if c.isalpha():
                keyTemp += c
        self.key = keyTemp.lower()
        self.key.translate(self.translationTable)
        self.decypher()

    @pyqtSlot(int)
    def setKeyOffset(self,keyOffset):
        self.keyOffset = keyOffset
        self.decypher()

class PlainTextAttackVigenere(QObject):
        translationTable = None
        cypheredText = ''
        clearText = ''
        key = ''
        keyCalculated = pyqtSignal(object)

        def __init__(self):
            '''
            Constructor
            '''
            QObject.__init__(self)
            self.cypheredText = ''
            self.translationTable = ''.maketrans('éèêëàâïîùûüöôç','eeeeaaiiuuuooc')

        @pyqtSlot(str)
        def setCypheredText(self,cypheredText):
            tempText = ''
            for c in cypheredText:
                if c.isalpha():
                    tempText += c
            self.cypheredText = tempText.lower()
            self.cypheredText.translate(self.translationTable)
            self.calculateKey()

        @pyqtSlot(str)
        def setClearText(self,clearText):
            tempText = ''
            for c in clearText:
                if c.isalpha():
                    tempText += c
            self.clearText = tempText.lower()
            self.clearText.translate(self.translationTable)
            self.calculateKey()

        def calculateKey(self):
            self.key = ''
            for index in range(0,min(len(self.cypheredText),len(self.clearText))):
                self.key += chr((ord(self.cypheredText[index]) - ord(self.clearText[index]))%26 + 97)
            self.keyCalculated.emit(self.key)
