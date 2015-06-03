'''
Created on 10 sept. 2013

@author: miistair
'''

from PyQt4.QtCore import QObject, pyqtSlot, pyqtSignal, Qt
# from collections import dict

class MonoAlphabeticSubstitutionAttack(QObject):
    textDecyphered = pyqtSignal(object) 
    letterFrequenciesCalculated = pyqtSignal(object)
    digramFrequenciesCalculated = pyqtSignal(object)
    trigramFrequenciesCalculated = pyqtSignal(object)
    
    def __init__(self):
        '''
        Constructor
        '''
        QObject.__init__(self)
        self.cypheredText = ''
        self.charA = ''
        self.charB = ''
        self.substitutionListWidget = None
        
    @pyqtSlot()
    def setCypheredText(self):
        self.cypheredText = self.sender().toPlainText()
        self.charFrom = ''
        self.charTo = ''
        done = ''
        for c in self.cypheredText:
            if c not in done and not (c is ' ' or c is '\n' or c is '\r' or c is '\t'):
                self.charFrom += c
                self.charTo += '-'
                done += c
        self.characterFrequencies()
        self.decypher()
        
    def setSubstitutionListWidget(self,listWidget):
        self.substitutionListWidget = listWidget
        self.substitutionListWidget.itemDoubleClicked.connect(self.removeSelectedItem)
        
    def decypher(self):
        charFrom = self.charFrom
        charTo = self.charTo
        for listItem in self.substitutionListWidget.findItems('->', Qt.MatchContains):
            charFrom += listItem.text()[0]
            charTo += listItem.text()[-1]
            
        substitutionTable = ''.maketrans(charFrom,charTo)
        clearText = self.cypheredText.translate(substitutionTable)
        self.textDecyphered.emit(clearText)
    
    @pyqtSlot(str)
    def setCharA(self,charA):
        if not (charA is ' ' or charA is '\n' or charA is '\r' or charA is '\t'):
            self.charA = charA
    
    @pyqtSlot(str)
    def setCharB(self,charB):
        if not (charB is ' ' or charB is '\n' or charB is '\r' or charB is '\t'):
            self.charB = charB
    
    @pyqtSlot()
    def addSubstitution(self):
        if not (self.charA is '' or self.charB is '' ):
            found = False
            for item in self.substitutionListWidget.findItems('->', Qt.MatchContains):
                if item.text().startswith(self.charA):
                    item.setText(self.charA + "->" + self.charB)
                    found = True
            if not found:
                self.substitutionListWidget.addItem(self.charA + "->" + self.charB)
            self.decypher()
            self.charA = ''
            self.charB = ''
    
    @pyqtSlot()
    def removeSelectedItem(self):
        self.substitutionListWidget.takeItem(self.substitutionListWidget.currentRow())
        self.decypher()
        
    def characterFrequencies(self):
        mapCharOccurence = dict()
        total = 0
        
        'Letter frequencies'
        for letter in self.cypheredText:
            if not (letter is ' ' or letter is '\n' or letter is '\r' or letter is '\t'):
                total += 1
                if letter not in mapCharOccurence:
                    mapCharOccurence[letter]=self.cypheredText.count(letter)
        for c in mapCharOccurence.keys():
            mapCharOccurence[c] = mapCharOccurence[c] * (100/total)
        sortedFreq = sorted(mapCharOccurence.items(), key=lambda x: x[1], reverse=True)
        letterLabelText = 'Cyphered :\n'
        number = 0
        for couple in sortedFreq:
            if number < 6 :
                letterLabelText += couple[0] +'=' + str(couple[1])[0:4] + '\n'
                number += 1
            else:
                break
        self.letterFrequenciesCalculated.emit(letterLabelText)
        
        'Digram frequencies'
        mapDigramOccurence = dict()
        total = 0
        for i in range(0,len(self.cypheredText)-1):
            digram = self.cypheredText[i:i+2]
            if not (' ' in digram or '\n'in digram or '\r' in digram or '\t' in digram):
                total += 1
                if digram not in mapDigramOccurence:
                    mapDigramOccurence[digram]=self.cypheredText.count(digram)
        for digram in mapDigramOccurence.keys():
            mapDigramOccurence[digram] = mapDigramOccurence[digram] * (100/total)
        sortedFreq = sorted(mapDigramOccurence.items(), key=lambda x: x[1], reverse=True)
        digramLabelText = 'Cyphered :\n'
        number = 0
        for couple in sortedFreq:
            if number < 6 :
                digramLabelText += couple[0] +'=' + str(couple[1])[0:4] + '\n'
                number += 1
            else:
                break
        self.digramFrequenciesCalculated.emit(digramLabelText)
        
        'Trigram frequencies'
        mapTrigramOccurence = dict()
        total = 0
        for i in range(0,len(self.cypheredText)-2):
            trigram = self.cypheredText[i:i+3]
            if not (' ' in trigram or '\n'in trigram or '\r' in trigram or '\t' in trigram):
                total += 1
                if trigram not in mapTrigramOccurence:
                    mapTrigramOccurence[trigram]=self.cypheredText.count(trigram)
        for trigram in mapTrigramOccurence.keys():
            mapTrigramOccurence[trigram] = mapTrigramOccurence[trigram] * (100/total)
        sortedFreq = sorted(mapTrigramOccurence.items(), key=lambda x: x[1], reverse=True)
        trigramLabelText = 'Cyphered :\n'
        number = 0
        for couple in sortedFreq:
            if number < 6 :
                trigramLabelText += couple[0] +'=' + str(couple[1])[0:4] + '\n'
                number += 1
            else:
                break
        self.trigramFrequenciesCalculated.emit(trigramLabelText)