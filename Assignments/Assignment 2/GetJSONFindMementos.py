import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import requests
import re
import json
import urllib
import urllib.request


def genericErrorInfo():
   import os, sys
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
   print('\tERROR:', errorMessage)


with open("ModifiedURLList.txt") as ins:
    urlInput = []
    for line in ins:
        urlInput.append(line)

urlHead = "http://memgator.cs.odu.edu/timemap/json/"
jsonList = []

memList = []
urlCounter = 1
for url in urlInput:

    mem = requests.get(urlHead+url)
    if mem.status_code != 200:
        memList.append(0)
        print(urlCounter, ": ", mem.status_code)
        urlCounter += 1

    else:
        jsonFileName = "URL #" + str(urlCounter) + ".json"
        jResponse = json.loads(mem.text)
        jsonList.append(jResponse)
        print(jResponse, file=open(jsonFileName, "w+"))
        print(urlCounter, ": ", mem.status_code, "\n", jResponse)
        urlCounter += 1

for jEntry in jsonList:
    memList.append(len(jEntry['mementos']['list']))

sortedMemList = []
sortedMemList = sorted(memList)
mementos = []
mementos = list(set(sortedMemList))

memTrack =[[0 for x in range(2)] for y in range(len(mementos))]

for x in range(len(mementos)):
    memTrack[x][0] = mementos[x]

for y in range(len(mementos)):
    for x in range(len(sortedMemList)):
        if memTrack[y][0] == sortedMemList[x]:
            memTrack[y][1] += 1
print(memTrack)
print(memTrack, file=open("MementoURLTable.txt", "w"))
print(mementos)
