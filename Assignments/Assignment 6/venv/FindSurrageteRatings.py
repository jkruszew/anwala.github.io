def getData():
    uData = []
    countD1 = 0
    with open("ModifiedU.data") as fin:
        for x in fin:
            uData.append(x)
            countD1 += 1
    '''
    countD2 = 0
    for x in uData:
        print(x)
        countD2 += 1

    print(countD1, "   ",countD2)
    '''
    uDataSplit = []
    for x in uData:
        uDataSplit.append(x.split(" "))

    uDataSplit.sort()
    return uDataSplit


def printUserRatings(surragete, ratings):
    for x in ratings:
        temp = ''
        if surragete == x[0]:
            for y in x:
                temp = temp + y +" "
            print(temp, file=open("Sur" + surragete + "Ratings.txt", "a+"))


ratings = getData()
surragetes = []

with open("SurrageteList.txt") as inf:
    for x in inf:
        surragetes.append(x.rstrip('\n'))

for x in surragetes:
    printUserRatings(x,ratings)



