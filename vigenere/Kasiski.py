from fractions import gcd
import math

'''
Kasiski examination

@author: gbabin
'''

def computeKeyLength(text):
    bloc_length = 2
    p = []
    strippedText = stripText(text)
    for i in range(len(strippedText)-bloc_length):
        pos = strippedText.find(strippedText[i:i+bloc_length], i+1)
        if pos > -1:
            p.append(pos-i)
    length = len(p)
    i=0
    divisorsLists = dict()
    divisorsFound = []
    if length > 0:
        for v in p:
            if v not in divisorsLists:
                divisorsLists[v] = divisors(v)
            divisorsFound.append(divisorsLists[v])
        frequencies = dict()
        for valueList in divisorsFound:
            for value in valueList:
                if value not in frequencies:
                    frequencies[value] = 0
                frequencies[value] += 1
        #print (sorted(frequencies.items(),key=lambda x: x[1], reverse=True)[0][0])
        return sorted(frequencies.items(),key=lambda x: x[1], reverse=True)[0][0]
#         for pgcd in pgcdSet:
#             stat = 0
#             for v in p:
#                 if gcd(pgcd,v) == pgcd:
#                     stat += 1
#             print (str(stat/length))
#             if (stat/length >= 0.50):
#                 return pgcd
    else:
        return -1

def divisors(number):
    divisorsList = []
    for i in range(2,number):
        if number % i == 0:
            divisorsList.append(i)
    return divisorsList

def stripText(text):
    strippedText = ''
    for c in text:
        if c.isalpha():
            strippedText += c

    #print (strippedText)
    return strippedText
