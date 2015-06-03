import sys
import re
'Import Qt'
from PyQt4.QtGui import QTextEdit, QTabWidget, QApplication, QLineEdit, QSpinBox, QTextCursor, QPushButton, QListWidget, QLabel,QComboBox
from PyQt4.QtCore import QObject, pyqtSlot

'Custom Classes import'
from mainUi.uiParameter import Ui_tabWidget
from vigenere.VigenereAttack import VigenereWrap, PlainTextAttackVigenere
from alphabetic.MonoAlphabeticSubstitutionAttack import MonoAlphabeticSubstitutionAttack
from alphabetic.AlphabeticShiftingAttack import AlphabeticShiftingAttack



class ConnectorWrapper(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        self.subscribers = []
        
    @pyqtSlot()
    def sendChangedText(self):
        text = self.sender().toPlainText()
        for textEdit in self.subscribers:
            if not (text == textEdit.toPlainText()):
                textEdit.setText(text)
                textEdit.moveCursor(QTextCursor.End)
            
    
def main():
    'The application needed to manage the events'
    app = QApplication(sys.argv)
    'The Main Window'
    tabWidget = QTabWidget()
    uiParameter= Ui_tabWidget()
    uiParameter.setupUi(tabWidget)
    vigenere = VigenereWrap()
    plainTextAttack = PlainTextAttackVigenere()
    alphaShiftingAttack = AlphabeticShiftingAttack()
    alphaSubAttack = MonoAlphabeticSubstitutionAttack()
    
    'Gathering Ui Element'
    cypheredTextEdit_VIG = tabWidget.findChild(QTextEdit, name='cypheredTextEdit_VIG')
    cypheredTextEdit_RSA = tabWidget.findChild(QTextEdit, name='cypheredTextEdit_RSA')
    '    shifting Elements'
    cypheredTextEdit_SHI = tabWidget.findChild(QTextEdit, name='cypheredTextEdit_SHI')
    asciiOffsetSpinBox_SHI = tabWidget.findChild(QSpinBox, name='asciiOffsetSpinBox_SHI')
    decypheredTextEdit_SHI = tabWidget.findChild(QTextEdit, name='decypheredTextEdit_SHI')
    '    substitution Elements'
    cypheredTextEdit_SUB = tabWidget.findChild(QTextEdit, name='cypheredTextEdit_SUB')
    addSubstitutionButton_SUB = tabWidget.findChild(QPushButton, name='addSubstitutionButton')
    cypheredLetterLineEdit_SUB = tabWidget.findChild(QLineEdit, name='cypheredLetterLineEdit')
    decypheredLetterLineEdit_SUB = tabWidget.findChild(QLineEdit, name='decypheredLetterLineEdit')
    listWidget_SUB = tabWidget.findChild(QListWidget, name='substitutionList')
    decypheredTextEdit_SUB = tabWidget.findChild(QTextEdit, name='decypheredTextEdit_SUB')
    removeSelectedButton_SUB = tabWidget.findChild(QPushButton, name='removeSelectedButton')
    '    substitution labels'
    letterLabel_SUB = tabWidget.findChild(QLabel, name='cypheredLetterLabel')
    digramLabel_SUB = tabWidget.findChild(QLabel, name='cypheredDigramsLabel')
    trigramLabel_SUB = tabWidget.findChild(QLabel, name='cypheredTrigramsLabel')
    
    englishLabel_SUB = tabWidget.findChild(QLabel, name='englishLetterLabel')
    englishLabel_SUB.setText('English :\ne=12.02\nt=9.10\na=8.12\no=7.68\ni=7.31\nn=6.95\n')
    englishDigramLabel_SUB = tabWidget.findChild(QLabel, name='englishDigramsLabel')
    englishDigramLabel_SUB.setText('English :\nth=3.88\nhe=3.68\nin=2.28\ner=2.17\nan=2.14\nre=1.74\n')
    englishTrigramLabel_SUB = tabWidget.findChild(QLabel, name='englishTrigramsLabel')
    englishTrigramLabel_SUB.setText('English :\nthe=3.50\nand=1.59\ning=1.14\nher=0.82\nhat=0.65\nhis=0.59\n')
    
    frenchLabel_SUB = tabWidget.findChild(QLabel, name='frenchLetterLabel')
    frenchLabel_SUB.setText('French :\ne=17.71\ns=7.94\na=7.63\ni=7.53\nt=7.24\nn=7.10\n')
    frenchDigramLabel_SUB = tabWidget.findChild(QLabel, name='frenchDigramsLabel')
    frenchDigramLabel_SUB.setText('French :\nes=3.05\nle=2.46\nen=2.42\nde=2.15\nre=2.09\nnt=1.97\n')
    frenchTrigramLabel_SUB = tabWidget.findChild(QLabel, name='frenchTrigramsLabel')
    frenchTrigramLabel_SUB.setText('French :\nent=0.84\nque=0.69\nles=0.66\nede=0.62\ndes=0.53\nela=0.45\n')
    
    '    AES Elements'
    cypheredTextEdit_AES = tabWidget.findChild(QTextEdit, name='cypheredTextEdit_AES')
    cypheredTextEdit_DES = tabWidget.findChild(QTextEdit, name='cypheredTextEdit_DES')
    '    vigenere Elements'
    decypheredTextEdit_VIG = tabWidget.findChild(QTextEdit, name='decypheredTextEdit_VIG')
    keyLineEdit = tabWidget.findChild(QLineEdit, name='keyLineEdit')
    keyOffsetSpinBox = tabWidget.findChild(QSpinBox, name='keyOffsetSpinBox')
    cypheredTextLineEdit = tabWidget.findChild(QLineEdit, name='cypheredTextLineEdit')
    decypheredTextLineEdit = tabWidget.findChild(QLineEdit, name='decypheredTextLineEdit')
    keyResult = tabWidget.findChild(QLineEdit, name='keyResult')
    languageComboBox = tabWidget.findChild(QComboBox, name='languageComboBox')
    lengthSpinBox = tabWidget.findChild(QSpinBox, name='lengthSpinBox')
    bruteForceButton = tabWidget.findChild(QPushButton, name='bruteForceButton')
    keyFoundLabel = tabWidget.findChild(QLabel, name='keyFoundLabel')
    tryKeyButton = tabWidget.findChild(QPushButton, name='tryKeyButton')
    
    'Connection'
    'cypheredText to allCypheredText'
    cypheredTextEditList = tabWidget.findChildren(QTextEdit)
    connectorWrapper = ConnectorWrapper()
    for cypheredTextEdit in cypheredTextEditList:
        if re.match("^cyphered", cypheredTextEdit.objectName()):
            cypheredTextEdit.textChanged.connect(connectorWrapper.sendChangedText)
            connectorWrapper.subscribers.append(cypheredTextEdit)
    'vigenere bruteforce part'
    languageComboBox.activated.connect(vigenere.setLanguage)
    lengthSpinBox.valueChanged.connect(vigenere.setKeyLength)
    bruteForceButton.clicked.connect(vigenere.bruteForce)
    vigenere.keyWorkCracked.connect(keyFoundLabel.setText)
    tryKeyButton.clicked.connect(vigenere.tryKey)
    
    'vigenere Upper/Bottom part'
    keyLineEdit.textChanged.connect(vigenere.setKey)
    keyOffsetSpinBox.valueChanged.connect(vigenere.setKeyOffset)
    cypheredTextEdit_VIG.textChanged.connect(vigenere.setCypheredText)
    vigenere.textDecyphered.connect(decypheredTextEdit_VIG.setText)
    'vigenere plainText attack part'
    cypheredTextLineEdit.textChanged.connect(plainTextAttack.setCypheredText)
    decypheredTextLineEdit.textChanged.connect(plainTextAttack.setClearText)
    plainTextAttack.keyCalculated.connect(keyResult.setText)
    'alphabetical shifting'
    cypheredTextEdit_SHI.textChanged.connect(alphaShiftingAttack.setCypheredText)
    asciiOffsetSpinBox_SHI.valueChanged.connect(alphaShiftingAttack.setAsciiOffset)
    alphaShiftingAttack.textDecyphered.connect(decypheredTextEdit_SHI.setText)
    'alphabetical substitution'
    cypheredTextEdit_SUB.textChanged.connect(alphaSubAttack.setCypheredText)
    alphaSubAttack.setSubstitutionListWidget(listWidget_SUB)
    cypheredLetterLineEdit_SUB.textChanged.connect(alphaSubAttack.setCharA)
    decypheredLetterLineEdit_SUB.textChanged.connect(alphaSubAttack.setCharB)
    addSubstitutionButton_SUB.clicked.connect(alphaSubAttack.addSubstitution)
    addSubstitutionButton_SUB.clicked.connect(cypheredLetterLineEdit_SUB.clear)
    addSubstitutionButton_SUB.clicked.connect(decypheredLetterLineEdit_SUB.clear)
    alphaSubAttack.textDecyphered.connect(decypheredTextEdit_SUB.setText)
    alphaSubAttack.letterFrequenciesCalculated.connect(letterLabel_SUB.setText)
    alphaSubAttack.digramFrequenciesCalculated.connect(digramLabel_SUB.setText)
    alphaSubAttack.trigramFrequenciesCalculated.connect(trigramLabel_SUB.setText)
    removeSelectedButton_SUB.clicked.connect(alphaSubAttack.removeSelectedItem)
    
    
    tabWidget.show()
    app.exec_()
