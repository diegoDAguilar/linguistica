# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 11:24:21 2018

@author: Diego-Chop
"""
import csv
import os
import math

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
def readText(filename):
    f = open(filename)
    d = []
    for line in f:
        for word in line.split():
            d.append(word)
    
    return d
"""
Obtaines the full vector of matching history. This function is used x freqs
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
                    
                    
    #print countSports, countHealth, countSpace
    
    #Prints a message stating the topic.
    if countSports > max(countHealth, countSpace):
        #print 'El tema de la noticia son los DEPORTES'
        return list(set(machingSports))
    elif countHealth > max(countSports, countSpace):
        #print 'El tema de la noticia es la SALUD'
        return list(set(machingHealth))
    elif countSpace > max(countSports, countHealth):
        #print 'El tema de la noticia es el ESPACIO'
        return list(set(machingSpace))
    else:
        #print 'No se pudo garantizar el tema de la noticia'
        return []
    
"""
*Arg being the text plus n lists of words plus the actual lists plus the freqs
Checks whether a word belongs to a vector of words
Returns the theme of the article
"""
def classifierOneNews(*arg): 

    vectorOfWordsVectors = []
    countHealth = 0
    countSports = 0
    countSpace = 0
    tfIdfHealth = 0.0
    tfIdfSports = 0.0
    tfIdfSpace = 0.0
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
                        tfIdfHealth += calculateTf_Idf(j, arg[2], arg[5])
                        countHealth += 1
                        machingHealth.append(j)
                    elif k == 1:
                        tfIdfSports += calculateTf_Idf(j, arg[3], arg[6])
                        countSports += 1
                        machingSports.append(j)
                    elif k == 2:
                        tfIdfSpace += calculateTf_Idf(j, arg[4], arg[7])
                        countSpace += 1
                        machingSpace.append(j)
                    
                    #print j + ' SI es ' + str(arg[2 + k][l][0])
                else:
                    #print j + ' no es ' + str(arg[2 + k][l][0])
                    pass
                    
                    
    print "FRECUENCIAS(salud, deportes, espacio): ", countHealth, countSports, countSpace
    print "TFIDF(salud, deportes, espacio): ", tfIdfHealth, tfIdfSports, tfIdfSpace
    
    #Prints a message stating the topic.
    if countSports > max(countHealth, countSpace):
        print 'El tema de la noticia por FRECUENCIA son los DEPORTES'
        #print machingSports
    elif countHealth > max(countSports, countSpace):
        print 'El tema de la noticia por FRECUENCIA es la SALUD'
        #print machingHealth
    elif countSpace > max(countSports, countHealth):
        print 'El tema de la noticia por FRECUENCIA es el ESPACIO'
        #print machingSpace
    else:
        print 'No se pudo garantizar el tema de la noticia por FRECUENCIA'
    
    
    #Prints a message stating the topic TFIDF
    if tfIdfSports > max(tfIdfHealth, tfIdfSpace):
        print 'El tema de la noticia por TFIDF son los DEPORTES'
        #print machingSports
    elif tfIdfHealth > max(tfIdfSports, tfIdfSpace):
        print 'El tema de la noticia por TFIDF es la SALUD'
        #print machingHealth
    elif tfIdfSpace > max(tfIdfSports, tfIdfHealth):
        print 'El tema de la noticia por TFIDF es el ESPACIO'
        #print machingSpace
    else:
        print 'No se pudo garantizar el tema de la noticia por TFIDF'
    print machingSpace
def calculateTf_Idf(word, wordList, freqList):
    numDocs = 30
    wordProcessed = [word]
    
    tf = (freqList[wordList.index(wordProcessed)])
    #print wordProcessed, wordList, freqList
    idf = math.log10(numDocs/(freqList[wordList.index(wordProcessed)]))
    #print idf
    return (tf * idf)
    

  
def timesPerDoc(vectorOfFreq, csvWordsVector):
    #csvFreq = [0] * 
    csvFreq = [0] * len(csvWordsVector)
    cont = 0
    #For each word of csv
    for i in range(len(csvWordsVector)):
        cont +=1
        #print csvWordsVector[i][0]
        #For each word of the vector
        for word in vectorOfFreq:
            
            #print word
            #word = "pacientes"
            if word == csvWordsVector[i][0]:
                csvFreq[cont - 1] += 1
    #print vectorOfFreq
    #print csvFreq
    #print csvWordsVector
    return csvFreq

def main():
    csvRow, csvWordsVector = readCsv('InformeSalud2.csv')
    csvRow2, csvWordsVector2 = readCsv('InformeDeportes2.csv')
    csvRow3, csvWordsVector3 = readCsv('InformeEspacio2.csv')
    
    #print csvWordsVector
    vectorOfFreq = []
    vectorOfFreq2 = []
    vectorOfFreq3 = []
    
    for filename in os.listdir('./Salud/'):
        d = readText('./Salud/' + filename)
        vectorFreq = classifier(d, 3, csvWordsVector, csvWordsVector2, csvWordsVector3 )
        vectorOfFreq.extend(vectorFreq)
        #print vectorFreq
        
    #print vectorOfFreq
    freqHealth = timesPerDoc(vectorOfFreq, csvWordsVector)
    
    
        
    #print vectorOfFreq
    
    for filename in os.listdir('./Deportes/'):
        d = readText('./Deportes/' + filename)
        vectorFreq2 = classifier(d, 3, csvWordsVector, csvWordsVector2, csvWordsVector3 )
        vectorOfFreq2.extend(vectorFreq2)
        #print vectorFreq    
    freqSports = timesPerDoc(vectorOfFreq2, csvWordsVector2)
    
    
    for filename in os.listdir('./Espacio/'):
        d = readText('./Espacio/' + filename)
        vectorFreq3 = classifier(d, 3, csvWordsVector, csvWordsVector2, csvWordsVector3 )
        vectorOfFreq3.extend(vectorFreq3)
        #print vectorFreq    
    freqSpace = timesPerDoc(vectorOfFreq3, csvWordsVector3)
    
    
    d = readText('./Salud/' + 'SupresorCancer.txt')
    classifierOneNews(d, 3, csvWordsVector, csvWordsVector2, csvWordsVector3,
                      freqHealth, freqSports, freqSpace)
    
if __name__ == "__main__":
    main()
    

