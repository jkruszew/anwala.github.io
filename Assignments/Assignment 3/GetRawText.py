from boilerpipe.extract import Extractor


def genericErrorInfo():
   import os, sys
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   errorMessage = fname + ', ' + str(exc_tb.tb_lineno) + ', ' + str(sys.exc_info())
   print('\tERROR:', errorMessage)
   return errorMessage


urlList = []
with open("URLTable.txt") as inp:
    for line in inp:
        urlList.append(line)

htmlTable = [['' for x in range(2)] for y in range(len(urlList))]

for x in range(len(urlList)):
    htmlTable[x][0], temp, htmlTable[x][1] = urlList[x].split(' ')

htmlFile = "RawHtml.html"

for x in range(len(htmlTable)):
    try:
        htmlID = htmlTable[x][0]
        rawHtml = open(htmlID+htmlFile, "r").read()
        extractor = Extractor(extractor='ArticleExtractor', html=rawHtml)
        print(extractor.getText(), file=open(htmlID+"RawText.txt", "w+"))
        print(htmlID, " Success")
    except:
        htmlID = htmlTable[x][0]
        print(genericErrorInfo(), file=open(htmlID+"RawText.txt", "w+"))
        print(htmlID, " Failed")
        genericErrorInfo()
