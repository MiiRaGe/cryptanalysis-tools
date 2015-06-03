from fractions import gcd
import math

'''
Coïncidence examination

@author: miistair
'''

'Indice de coincidence aléatoire'
Ia = 1/26
'Indice de coincidence du français'
If = 0.0746
'Indice de coincidence de l\'anglais'
Ie = 0.0667
def computeKeyLength(text):
    strippedText = stripText(text)
    coincidenceList = dict()
    for i in range(2,min(50,len(text)//2)):
        coincidenceList[i] = textCoincidence(strippedText,i)
#     coincidenceList = dict()
#     for i in range(2,len(text)//2):
#         n = len(strippedText)
#         coincidence = (If - Ia)*n + i*(n*Ia - If)
#         coincidence = coincidence /( i * (n -1))
#         coincidenceList[i] = coincidence
    sortedList = sorted(coincidenceList.items(),key=lambda x: x[1], reverse=True)
    i = 0
    while (sortedList[i][0] > sortedList[i+1][0] and ((sortedList[i][1] - sortedList[i+1][1])/sortedList[i][1] < 0.20)):
        i += 1
    return sorted(coincidenceList.items(),key=lambda x: x[1], reverse=True)[i][0]
    
def textCoincidence(text, keyLength):
    coincidenceList = []
    for i in range(0,min([keyLength,len(text)])):
        textPart = text[i::keyLength]
        if textPart is not '':
            coincidenceList.append(characterFrequencies(textPart))
        
    return sum(coincidenceList)/len(coincidenceList)
    
def characterFrequencies(text):
    mapCharOccurence = dict()
    total = 0
    'Letter frequencies'
    for letter in text:
        total += 1
        if letter not in mapCharOccurence:
            mapCharOccurence[letter]=text.count(letter)
    if total > 1:
        for c in mapCharOccurence.keys():
            mapCharOccurence[c] = (mapCharOccurence[c] * (mapCharOccurence[c] - 1))/(total * (total -1))
        
    coincidence = 0
    for value in mapCharOccurence.values():
        coincidence += value
    return (coincidence)
    
def stripText(text):
    strippedText = ''
    for c in text:
        if c.isalpha():
            strippedText += c
    return strippedText
