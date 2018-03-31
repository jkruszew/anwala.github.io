def getItems():
    uItem = []
    countI1 = 0
    with open("ModifiedU.item") as fin:
        for x in fin:
            uItem.append(x)
            countI1 += 1
    '''
    countI2 = 0
    for x in uItem:
        print(x)
        countI2 += 1

    print(countI1, "   ",countI2)
    '''
    uItemSplit = []
    for x in uItem:
        uItemSplit.append(x.split("|"))

    return uItemSplit


def getSurragetes():
    surragetes = []
    with open("SurrageteList.txt") as inf:
        for x in inf:
            surragetes.append(x.rstrip('\n'))
    return surragetes


def getSurrageteTopRatings(surragetes):
    surrageteRatings = []
    for x in surragetes:
        with open("Sur"+x+"TopRatings.txt") as inf:
            for y in inf:
                surrageteRatings.append(y.rstrip('\n'))
    return surrageteRatings


def getSurrageteBotRatings(surragetes):
    surrageteRatings = []
    for x in surragetes:
        with open("Sur"+x+"BotRatings.txt") as inf:
            for y in inf:
                surrageteRatings.append(y.rstrip("\n"))
    return surrageteRatings


def getTopMovieTitles(ratings, movies):
    for x in ratings:
        counter = 0
        tempX = x.split(' ')
        temp = ''
        for y in movies:
            if tempX[1] == y[0]:
                for z in y:
                    temp = temp + z + "|"
                if counter % 2 == 0:
                    print(temp[:-1], file=open("Sur"+tempX[0]+"TopMovies.txt", "a+"))
                counter = counter + 1


def getBotMovieTitles(ratings, movies):
    for x in ratings:
        counter = 0
        tempX = x.split(' ')
        temp = ''
        for y in movies:
            if tempX[1] == y[0]:
                for z in y:
                    temp = temp + z + "|"
                if counter % 2 == 0:
                    print(temp[:-1], file=open("Sur"+tempX[0]+"BotMovies.txt", "a+"))
                counter = counter + 1


movies = getItems()
surragetes = getSurragetes()
surrageteTopRatings = getSurrageteTopRatings(surragetes)
surrageteBotRatings = getSurrageteBotRatings(surragetes)

getTopMovieTitles(surrageteTopRatings,movies)
getBotMovieTitles(surrageteBotRatings,movies)

'''for x in surrageteTopMovies:
    print(surrageteTopMovies)
'''
'''for x in surrageteBotRatings:
    print(x)
'''


