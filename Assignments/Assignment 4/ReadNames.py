friendCountIn = []

with open("friendCount.txt") as inf:
    for x in inf:
        friendCountIn.append(x)

fCount = []
for x in range(len(friendCountIn)):
    num = friendCountIn[x].split(' ')
    fCount.append(num[-1])

fList = []
for x in range(len(fCount)):
    fCount[x] = fCount[x].strip()
    fList.append(int(fCount[x]))

print(fList)
print(fCount)
fList.sort()
print(fList)

outFile = [['' for x in range(2)] for y in range(len(fList)+3)]
print(outFile)
for x in range(len(outFile)):
    if x < 10:
        outFile[x][1] = fList[x]
        outFile[x][0] = x
    elif x == 10:
        outFile[x][1] = 98
        outFile[x][0] = x
    elif x > 10  and x < 49:
        outFile[x][1] = fList[x-1]
        outFile[x][0] = x
    elif x == 49:
        outFile[x][1] = 396
        outFile[x][0] = x
    elif x > 49 and x < 62:
        outFile[x][1] = fList[x-2]
        outFile[x][0] = x
    elif x == 62:
        outFile[x][1] = 539.43373852397
        outFile[x][0] = x
    elif x == 63:
        outFile[x][1] = 542.6734693877551
        outFile[x][0] = x
    else:
        outFile[x][1] = fList[x-3]
        outFile[x][0] = x
print(outFile)

for x in range(len(outFile)):
    print(outFile[x][0]," ",outFile[x][1], file=open("SortedFriendList.txt","a+"))
    print(outFile[x][0], " ", outFile[x][1])

'''mean = 0
median = 0
stdDiv = 0
count = 0

for x in range(len(fList)):
    count += 1
    mean += fList[x]


median = (fList[int(count/2)-1]+fList[int((count+2)/2)-1])/2


print(count)
print(mean/count)
print(median)

prints = ""
for x in fList:
    prints = prints+str(x)+","

print(prints)
'''