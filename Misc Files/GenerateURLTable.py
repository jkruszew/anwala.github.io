urlList = []
with open("ModifiedURLList.txt", "r") as inp:
    for url in inp:
        urlList.append(url)

for x in range(len(urlList)):
    print("U" + str(x) + " ", urlList[x], end='')
    print("U" + str(x) + " ", urlList[x], end='', file=open("URLTable.txt", "a+"))
