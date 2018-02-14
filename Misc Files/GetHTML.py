import requests


def genericErrorInfo():
   import os, sys
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   errorMessage = fname + ', ' + str(exc_tb.tb_lineno) + ', ' + str(sys.exc_info())
   print('\tERROR:', errorMessage)


urlList = []
with open("URLTable.txt") as inp:
    for line in inp:
        urlList.append(line)

urlTable = [['' for x in range(2)] for y in range(len(urlList))]

for x in range(len(urlList)):
    urlTable[x][0], temp, urlTable[x][1] = urlList[x].split(' ')


for x in range(len(urlTable)):
    try:
        uHTML = requests.get(urlTable[x][1]).text
        urlID = urlTable[x][0]
        #uHTML = requests.get("http://www.odu.edu/compsci").text
        print(uHTML, file=open(urlID+"RawHtml.txt", "w+"))

    except:
        genericErrorInfo()

    if x == 2:
        break