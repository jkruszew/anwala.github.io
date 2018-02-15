import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def genericErrorInfo():
   import os, sys
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
   #print('\tERROR:', errorMessage)


inputFile = "InitialURLList.txt"
#inputFile = "Output.txt"
tString = "https://twitter.com"
inCount = 1
with open(inputFile, "r") as ins:
   urlInput = []
   for line in ins:
       if line[:19].lower() != tString:
           urlInput.append(line)
           #print("Reading input: ", inCount)
           #inCount += 1


urlList = list(set(urlInput))

count = 1
for url in urlList:
   print(count, ": ", url)
   count += 1

urlListExpanded = []

count2 = 1
urlCounter = 1
goodUrlCounter = 0
badUrlCounter = 0
for url in urlList:
   print("checking urls for status code and expanded url", urlCounter)
   urlCounter += 1
   try:
       r = requests.get(url, verify=False, allow_redirects=True)
       if int(r.status_code) == 200:
           urlListExpanded.append(r.url)
           goodUrlCounter += 1
           print("url added to list, Status Code: ", r.status_code, "total urls added: ", goodUrlCounter)
           print("\t", r.url)
       else:
           badUrlCounter += 1
           print("url not added to list, Status Code: ", r.status_code, "total rejected urls: ", badUrlCounter)
   except:
       genericErrorInfo()
       badUrlCounter += 1
       print("Error Occurred, URL not Added to List total rejected urls: ", badUrlCounter)
       continue
   urlListExpanded = list(set(urlListExpanded))
   if len(urlListExpanded) == 1000:
       break

urlListExpanded = list(set(urlListExpanded))
for url in urlListExpanded:
    print(url, file=open("ModifiedURLList.txt", "a"))

'''
for url in urlListExpanded:
   print(count2, ": ", url)
   print(url, file=open("ModifiedURLList.txt", "a"))
   count2 += 1

'''
