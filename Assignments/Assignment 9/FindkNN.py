import clusters
import numpredict

def getBlogData(f = 'f-mesureData.txt'):
    retval = []

    with open(f) as inf:
        tempData = []
        for x in inf:
            tempData =(x.split('\t'))

        for x in tempData:
            retval.append(float(x))

    return retval


def getData(f = 'blogdata1 (copy).txt'):
    name, word, data = clusters.readfile(f)
    return data


def getNames(f = 'blogdata1 (copy).txt'):
    name, word, data = clusters.readfile(f)
    return name


def getWords(f = 'blogdata1 (copy).txt'):
    name, word, data = clusters.readfile(f)
    return word


def getkNN(data, bName, bData):
    k = [1,2,5,10,20]

    for x in k:
        neighbors = numpredict.knnestimate(data, bData, x)

        print("Nearest Neighbors For ", bName, "(k = ", x, ")")
        print("Nearest Neighbors For ", bName, "(k = ", x, ")", file = open(str(bName)+".txt", 'a+'))

        for y in neighbors:
            nIndex = y[1]
            nName = names[nIndex]

            print("\t", nName, "\t---\t", y[0])
            print("\t", nName, "\t---\t", y[0], file = open(str(bName) + ".txt", 'a+'))

        print("")
        print("", file = open(str(bName) + ".txt", 'a+'))


data = getData()
names = getNames()

bData = getBlogData()
blog1 = "F-Measure"
getkNN(data, blog1, bData)

bData = getBlogData('ws-dlData.txt')
blog2 = "Web Science and Digital Libraries Research Group"
getkNN(data, blog2, bData)




