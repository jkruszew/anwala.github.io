def getUsers():
    uUser = []
    countU1 = 0
    with open("ModifiedU.user") as fin:
        for x in fin:
            uUser.append(x)
            countU1 += 1

    '''
    countU2 = 0
    for x in uUser:
        print(x)
        countU2 += 1

    print(countU1, "   ",countU2)
    '''

    uUserSplit = []
    for x in uUser:
        uUserSplit.append(x.split(" "))

    return uUserSplit


def findSurrages(users):
    me = [26, "M", "student"]
    surragetes = []
    for x in users:
        if (me[0] == int(x[1])) and (me[1] == x[2]) and (me[2] == x[3]):
            surragetes.append(x)
    return surragetes


users = getUsers()

surragetes = findSurrages(users)

for x in surragetes:
    temp = ""
    for y in x:
        temp = temp + y + " "
    print(temp, file=open("Sur" + x[0] + ".txt", "a+"))
    print(x[0], file=open("SurrageteList.txt", ("a+")))