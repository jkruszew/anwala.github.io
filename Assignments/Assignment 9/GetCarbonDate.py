import requests
import re
import json
import urllib
import urllib.request
import datetime
from datetime import date


def genericErrorInfo():
   import os, sys
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
   print('\tERROR:', errorMessage)


def getCarbonDate(url,urlNum):
    try:
        carbonURL = "http://localhost:8888/cd/"
        carbonDateURL = carbonURL + url
        carbonDateRequest = requests.get(carbonDateURL)
        carbonDateData = json.loads(carbonDateRequest.text)
        estDate = carbonDateData['estimated-creation-date']
        if estDate == '':
            print(urlNum, ": No Date")
            print(carbonDateData, file=open("U" + str(urlNum) + "CarbonDate.json", "w+"))
        else:
            print(urlNum, ": ", str(estDate)[:10])
            print(carbonDateData, file=open("U"+ str(urlNum) + "CarbonDate.json", "w+"))
        return str(estDate)[:10]
    except:
        genericErrorInfo()
        return ''




def getMementos(url, urlNum):
    mementoURL = "http://memgator.cs.odu.edu/timemap/json/"
    memURL = mementoURL + url

    try:
        memRequest = requests.get(memURL)

        if memRequest.status_code != 200:
            print(0)
            print("", file=open("U"+ str(urlNum) + "TimeMap.json", "w+"))
            return 0
        else:
            jResponse = json.loads(memRequest.text)
            print(len(jResponse['mementos']['list']))
            print(jResponse, file=open("U"+ str(urlNum) + "TimeMap.json", "w+"))
            return len(jResponse['mementos']['list'])
    except:
        genericErrorInfo()
        return 0


def calculateDays(carbonDate):
    year = int(carbonDate[0:4])
    month = int(carbonDate[5:7])
    day = int(carbonDate[8:10])
    cDate = date(year,month,day)

    now = datetime.datetime.now()
    currentDate = date(now.year, now.month, now.day)

    val = currentDate - cDate

    retVal = str(val).split(' ')

    if now.year == year and now.month == month and now.day == day:
        retVal = str(1)

    return int(retVal[0])


with open("ModifiedURLList.txt") as ins:
    urlInput = []
    for line in ins:
        urlInput.append(line)

carbonDateList = []
mementoList = []
urlAge = []
carbonDateWithmemAgeList = []
carbonDateWithMemList = []
noMementosCounter = 0
noCarbonDateCounter = 0

mementoCounter = 0
carbonDateCounter = 0

for urlNum in range(len(urlInput)):
    try:
        carbonDateList.append(getCarbonDate(urlInput[urlNum], urlNum))
        mementoList.append(getMementos(urlInput[urlNum], urlNum))
    except:
        genericErrorInfo()

for x in range(len(carbonDateList)):
    print(carbonDateList[x])
    print(mementoList[x])

for x in carbonDateList:
    if x == '':
        urlAge.append(1)
    else:
        urlAge.append(calculateDays(x))

for x in range(len(urlAge)):
    print(x, ": ", urlAge[x])

print()

for x in range(len(urlAge)):
    if urlAge[x] == 1:
        noCarbonDateCounter += 1
    else:
        carbonDateCounter += 1

    if mementoList[x] == 0:
        noMementosCounter += 1
    else:
        mementoCounter += 1


print()

print("No Date: ", noCarbonDateCounter)
print("Date:    ", carbonDateCounter)
print("Total D: ", noCarbonDateCounter+carbonDateCounter)

print()

print("No Mem:  ", noMementosCounter)
print("Mem:     ", mementoCounter)
print("Total M: ", noMementosCounter+mementoCounter)

for x in range(len(urlAge)):
    if urlAge[x] > 1 and mementoList[x] > 0:
        carbonDateWithmemAgeList.append(urlAge[x])
        carbonDateWithMemList.append(mementoList[x])


memAgeList = [[0 for x in range(len(carbonDateWithMemList))] for y in range(2)]

for x in range(len(carbonDateWithMemList)):
    memAgeList[0][x] = carbonDateWithMemList[x]
    memAgeList[1][x] = carbonDateWithmemAgeList[x]


print()
print("Mementos\tAge")
for x in range(len(carbonDateWithmemAgeList)):
    print(memAgeList[0][x], "\t\t", memAgeList[1][x])
    print(memAgeList[0][x], " ", memAgeList[1][x], file=open("MementoAgeList.txt", "a+"))

print("Total URIs:          ", noMementosCounter+mementoCounter)
print("No Mementos:         ", noMementosCounter)
print("No Date Estimation:  ", noCarbonDateCounter)

print("Total URIs:          ", noMementosCounter+mementoCounter, file=open("Part3.txt", "a+"))
print("No Mementos:         ", noMementosCounter, file=open("Part3.txt", "a+"))
print("No Date Estimation:  ", noCarbonDateCounter, file=open("Part3.txt", "a+"))

