# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 11:24:21 2018

@author: Diego-Chop
"""
import csv


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
    f = open('noticiaPrueba3.txt')
    d = []
    for line in f:
        for word in line.split():
            d.append(word)
    
    return d
"""
*Arg being the text plus n lists of words plus the actual lists
Checks whether a word belongs to a vector of words
Returns the theme of the article
"""
def classifier(*arg): 

    vectorOfWordsVectors = []
    countHealth = 0
    countSports = 0
    countSpace = 0
    machingHealth = []
    machingSports = []
    machingSpace = []
    
    #Contains n elements. Each element being a vector of words from the csv    
    for i in range(0, arg[1]):
        vectorOfWordsVectors.append(arg[2 + i])
        
    #For each word of the text
    for j in arg[0]:
        #For each vector of words from the csv
        for k in range(0, arg[1]):
            #For each element of the vector of words from the csv
            for l in range(0, len(arg[2 + k])):
                if j == arg[2 + k][l][0]:
                    if k == 0:
                        countHealth += 1
                        machingHealth.append(j)
                    elif k == 1:
                        countSports += 1
                        machingSports.append(j)
                    elif k == 2:
                        countSpace += 1
                        machingSpace.append(j)
                    
                    #print j + ' SI es ' + str(arg[2 + k][l][0])
                else:
                    #print j + ' no es ' + str(arg[2 + k][l][0])
                    pass
                    
                    
    print countSports, countHealth, countSpace
    
    #Prints a message stating the topic.
    if countSports > max(countHealth, countSpace):
        print 'El tema de la noticia son los DEPORTES'
        print machingSports
    elif countHealth > max(countSports, countSpace):
        print 'El tema de la noticia es la SALUD'
        print machingHealth
    elif countSpace > max(countSports, countHealth):
        print 'El tema de la noticia es el ESPACIO'
        print machingSpace
    else:
        print 'No se pudo garantizar el tema de la noticia'
    
def main():
    csvRow, csvWordsVector = readCsv('InformeSalud.csv')
    csvRow2, csvWordsVector2 = readCsv('InformeDeportes.csv')
    csvRow3, csvWordsVector3 = readCsv('InformeEspacio.csv')
    

    d = readText()

    classifier(d, 3, csvWordsVector, csvWordsVector2, csvWordsVector3 )
    
if __name__ == "__main__":
    main()
