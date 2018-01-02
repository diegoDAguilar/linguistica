# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 11:24:21 2018

@author: Diego-Chop
"""
import csv
#INPUT: n documentos, m grupos, los vectores de cada grupo

#Para cada documento, comprobar si cada palabra del texto corresponde a un 
#vector, si corresponde aniade un contador a ese grupo


"""
Reads from InformeSalud.csv and returns csvNTimes and csvWordsVector
csvNTimes is an array with the number of times a word appears
csvWordsVector is an array with the words

"""

def readCsv(fileName):
    file = open(fileName)
    reader = csv.reader(file)
    csvNTimes = []
    csvWordsVector = []
    next(reader)
    
    for row in reader:
        csvValue1 = int(row[1])
        csvValue0 = row[0]
        csvNTimes.append([csvValue1])
        csvWordsVector.append([csvValue0])
    
    return (csvNTimes, csvWordsVector)

"""
Reads noticiaPrueba.txt and returns an array d with every word
"""
def readText():
    f = open('noticiaPrueba2.txt')
    d = []
    for line in f:
        for word in line.split():
            d.append(word)
    
    return d
"""
#Arg being the text plus n lists of words
"""
def classifier(*arg): 

    vectorOfWordsVectors = []
    cont = 0
    cont2 = 0
    countHealth = 0
    countSports = 0
    
    #Contains n elements. Each element being a vector of words from the csv    
    for i in range(0, arg[1]):
        vectorOfWordsVectors.append(arg[2 + i])
    #For each word of the text
    for j in arg[0]:
        #cont += 1
        #For each vector of words from the csv
        for k in range(0, arg[1]):
            #cont2 += 1
            #For each element of the vector of words from the csv
            #print len(arg[2 + k])
            for l in range(0, len(arg[2 + k])):
                if j == arg[2 + k][l][0]:
                    print 'igual'
                    if k == 0:
                        countHealth += 1
                    elif k == 1:
                        countSports += 1
                    
                    #print j + ' SI es ' + str(arg[2 + k][l][0])
                else:
                    print j + ' no es ' + str(arg[2 + k][l][0])
                    pass
                    
                    
    print countSports, countHealth
    #print cont, cont2

    
def main():
    csvRow, csvWordsVector = readCsv('InformeSalud.csv')
    csvRow2, csvWordsVector2 = readCsv('InformeDeportes.csv')
    
    #print csvWordsVector
    
    #print csvRow[5]
    #print csvWordsVector[5]
    #print csvWordsVector
    d = readText()
    #print d
    classifier(d, 2, csvWordsVector, csvWordsVector2 )
    
if __name__ == "__main__":
    main()
    


#OUTPUT: imprimir por pantalla a que m-grupo pertenecen los n documentos.