import csv
import os
import itertools
import ast
verbose = False
global reader
reader = csv.reader('')
dataPath = '/data/'
# fileWriter = csv.writer(open(curdir+currentFileName, 'w'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# fileWriter.writerow(writeThis)

def getOPENfile(fileName):
    print(fileName)
    return open(fileName, 'r')

def getCSVreader(fileName):
    reader = csv.reader(getOPENfile(fileName))
    if(verbose):
        for row in reader:
            print(row)
    return reader

def getCSVreaderHeader(reader):
    """Returns first row of CSV Reader, the Header."""
    return reader.next()

if __name__=="__main__":
    import subprocess as sp
    #sp.call('cls',shell=True)
    tmp = sp.call('clear',shell=True)
    dataPath = '../data'
    dataPath = 'Digital_Multi_Tool_w_ESP32/data/dance'
    print(os.getcwd()) 
    print(os.listdir(dataPath))
    


