def getSurragetes():
    surragetes = []
    with open("SurrageteList.txt") as inf:
        for x in inf:
            surragetes.append(x.rstrip('\n'))
    return surragetes


def getSurrageteRatings(surragetes):
    retVal = []
    for x in surragetes:
        with open("Sur"+x+"TopRatings.txt") as inf:
            for y in inf:
                retVal.append((y.rstrip('\n')).split(' '))
        with open("Sur"+x+"BotRatings.txt") as inf:
            for y in inf:
                retVal.append((y.rstrip('\n')).split(' '))
    return retVal


def getSurrageteMovies(surragete):
    retVal = []
    with open("Sur" + surragete + "TopMovies.txt") as inf:
        for y in inf:
            retVal.append((y.rstrip('\n')).split('|'))
    with open("Sur" + surragete + "BotMovies.txt") as inf:
        for y in inf:
            retVal.append((y.rstrip('\n')).split('|'))
    return retVal


def printMoviesWithRatings(ratings):
    for x in ratings:
        temp = ''
        movies = getSurrageteMovies(x[0])
        for y in movies:
            if x[1] == y[0]:
                temp = x[0] + "|" + y[1] + "|" + x[2]
        print(temp, file=open("Sur"+x[0]+"TopBottomMovies.txt", "a+"))




surragetes = getSurragetes()

ratings = getSurrageteRatings(surragetes)


printMoviesWithRatings(ratings)
