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


def calculateDays(carbonDate):
    now = datetime.datetime.now()
    year = int(carbonDate[0:4])
    month = int(carbonDate[5:7])
    day = int(carbonDate[8:10])
    cDate = date(year,month,day)
    currentDate = date(now.year, now.month, now.day)

    retval = currentDate - cDate
    return retval



with open("ModifiedURLList.txt") as ins:
    urlInput = []
    for line in ins:
        urlInput.append(line)

carbonURL = "http://localhost:8888/cd/"
#carbonJsonList = []
carbonDateList = []
carbonCounter = 0
noCarbonCounter = 0

mementoURL = "http://memgator.cs.odu.edu/timemap/json/"
mementoList = []
#mementoJsonList = []
mementoCounter = 0
noMementoCounter = 0

noMemWithCarbonIndexList = []

index = 1
for url in urlInput:
    carbonDateURL = carbonURL + url
    mem = requests.get(mementoURL+url)

    carbonDateRequest = requests.get(carbonDateURL)
    carbonDateData = carbonDateRequest.json()
    # carbonJsonList.append(carbonDateData)
    estDate = carbonDateData['estimated-creation-date']

    if estDate == '':
        carbonDateList.append(str(estDate))
        print("No Date")
    else:
        carbonDateList.append(str(estDate)[0:10])
        print(str(estDate)[:10])

    if mem.status_code != 200:
        mementoList.append(0)
        print(0)
    else:
        jResponse = json.loads(mem.text)
        mementoList.append(len(jResponse['mementos']['list']))
        # mementoJsonList.append(jResponse)
        print(len(jResponse['mementos']['list']))


for x in range(len(carbonDateList)):
    if carbonDateList[x] == '':
        noCarbonCounter += 1
    else:
        carbonCounter += 1
        if mementoList[x] == 0:
            noMemWithCarbonIndexList.append(x)


    if mementoList[x] == 0:
        noMementoCounter += 1
    else:
        mementoCounter += 1


daysLivedList = []
for x in noMemWithCarbonIndexList:
    days = calculateDays(carbonDateList[x])
    daysLivedList.append(days)

print("\n\n\n\n\n")
for x in daysLivedList:
    print(x)
