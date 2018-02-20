'''
from goose3 import Goose
import requests

uHTML = requests.get("http://www.odu.edu/compsci").text
print(uHTML, file=open("OduCsTestRawHtml.html", "w+"))
#print(uHTML)
print(uHTML)
test = open("OduCsTestRawHtml.html").read()

print(test)
#print(htmlStr)

g = Goose()

content = g.extract(url="http://www.odu.edu/compsci")
print(content.title)
print(content.cleaned_text)

from boilerpipe.extract import Extractor
import requests

uHTML = requests.get("http://www.odu.edu/compsci").text
print(uHTML, file=open("OduCsTestRawHtml.html", "w+"))
#print(uHTML)
html = open("OduCsTestRawHtml.html").read()
#print(html)
extractor = Extractor(extractor='ArticleExtractor', html=html)
print(extractor.getText())
extractor = Extractor(extractor='ArticleExtractor', url="http://www.odu.edu/compsci")
print(extractor.getText())
'''

'''
U = 1000
oS = "grep -i -c \"Sport\" "
print(oS)
for x in range(U):
    oS = oS + ("U"+str(x)+"RawText.txt ")

oS = oS + "> grepOutput.txt"
print(oS)
'''
urlList = []
with open("grepOutput.txt") as inf:
    for x in inf:
        urlList.append(x);

for x in range(len(urlList)):
    urlList[x] = urlList[x].split(':')
    urlList[x][1],discard = urlList[x][1].split('\n')
    urlList[x][1] = int(urlList[x][1])
urls = []
for x in range(len(urlList)):
    urlN, discard = urlList[x][0].split("RawText.txt")
    urls.append(urlN)
    if urlList[x][1] != 0:
        print(urls[x])
        print(urls[x], file=open("grepOutputTrimmedUrlID.txt", "a+"))

for x in range(len(urlList)):
    if urlList[x][1] != 0:
        print(urlList[x][0]+":"+str(urlList[x][1]))
        print(urlList[x][0]+"\t"+str(urlList[x][1]), file=open("grepOutputTrimmed.txt", "a+"))