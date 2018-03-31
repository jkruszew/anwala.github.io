def printBotRated(ratingsList):
    for x in ratingsList:
        temp = ''
        if x[2] == '1':
            for y in x:
                temp = temp + y + " "
            #print(temp)
            print(temp, file=open("Sur"+x[0]+"BotRatings.txt", "a+"))


def getSurragetes():
    surragetes = []
    with open("SurrageteList.txt") as inf:
        for x in inf:
            surragetes.append(x.rstrip('\n'))
    return surragetes


def getSurrageteRatings(surragetes):
    ratings = []
    for x in surragetes:
        with open("Sur" + x + "Ratings.txt") as inf:
            for y in inf:
                ratings.append((y.rstrip('\n')).split(' '))

    for x in ratings:
        ratings.remove(['', ''])
    return ratings


surragetes = getSurragetes()
ratings = getSurrageteRatings(surragetes)
printBotRated(ratings)

'''for x in ratings:
    print(x)
'''