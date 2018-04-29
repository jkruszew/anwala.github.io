import json
import re


oldPrefix = "/home/jonathan/PycharmProjects/Assignment9/OldTimeMaps/U"
oldSuffix = "TimeMap.json"
newPrefix = "/home/jonathan/PycharmProjects/Assignment9/NewTimeMaps/U"
newSuffix = "TimeMap.json"

oldMememtoCount = []
newMementoCount = []

for x in range(1000):
    test = []
    temp = ""

    with open(oldPrefix+str(x)+oldSuffix) as inF:
        temp = inF.read()
        #print(x,":  ", temp)
        test = [m.start() for m in re.finditer("datetime", temp)]
        #print(x,":  ", test)
        oldMememtoCount.append(len(test))

'''
for x in range(len(oldMememtoCount)):
    print(x,":  ",oldMememtoCount[x])
'''

for x in range(1000):
    test = []
    temp = ""

    with open(newPrefix+str(x)+newSuffix) as inF:
        temp = inF.read()
        #print(x,":  ", temp)
        test = [m.start() for m in re.finditer("datetime", temp)]
        #print(x,":  ", test)
        newMementoCount.append(len(test))

'''
print("X:  Old   New")
for x in range(len(newMementoCount)):
    print(x,":  ",oldMememtoCount[x],"   ",newMementoCount[x])
'''

deltaCount = []
for x in range(len(newMementoCount)):
    deltaCount.append(newMementoCount[x] - oldMememtoCount[x])

temp = ""
for x in range(len(deltaCount)):
    print(x,":  ",deltaCount[x])
    print(x, " ", deltaCount[x], file=open("TimestampDelta.txt", "a+"))


