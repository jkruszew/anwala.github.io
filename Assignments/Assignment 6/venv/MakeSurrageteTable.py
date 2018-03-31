def getSurragetes():
    surragetes = []
    with open("SurrageteList.txt") as inf:
        for x in inf:
            surragetes.append(x.rstrip('\n'))
    return surragetes


def getTopBottomRatings(surragetes):
    topBottomRatings = []
    for x in surragetes:
        with open("Sur"+x+"TopBottomMovies.txt") as inf:
            for y in inf:
                topBottomRatings.append((y.rstrip('\n')).split('|'))
    return topBottomRatings


def get3TopBottom(surragete, topBottomRatings):
    retVal = []
    for x in surragetes:
        topCounter = 0
        botCounter = 0
        for y in topBottomRatings:
            temp = ''
            if topCounter < 3 and y[2] == '5' and x == y[0]:
                temp = y[0] + "|" + y[1] + "|" + y[2]
                topCounter = topCounter + 1
                retVal.append(temp)
            if botCounter < 3  and y[2] == '1' and x == y[0]:
                temp = y[0] + "|" + y[1] + "|" + y[2]
                botCounter = botCounter + 1
                retVal.append(temp)
    return retVal

surragetes = getSurragetes()
topBottomRatings = getTopBottomRatings(surragetes)

topBottom3 = get3TopBottom(surragetes,topBottomRatings)

for x in topBottom3:
    print(x, file=open("SurragetesTopBottom3.txt", "a+"))
