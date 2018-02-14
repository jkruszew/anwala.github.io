'''urlList = []
with open("URLTable.txt") as inp:
    for line in inp:
        urlList.append(line)

urlTable = [['' for x in range(2)] for y in range(len(urlList))]

for x in range(len(urlList)):
    urlTable[x][0], temp, urlTable[x][1] = urlList[x].split(' ')

for x in range(len(urlList)):
    print(urlTable[x][1])
'''

test =[[0 for x in range(2)] for y in range(5)]

print(test)
print(len(test))
print(len(test[1]))
