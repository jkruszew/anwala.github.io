prefix = '/home/jonathan/PycharmProjects/Assignment7/CurlFiles/curlFile'
inF = []
for x in range(500):
    with open(prefix+str(x)+'.txt') as inFile:
        for y in inFile:
            inF.append(y)
            #print(y)

urls = []
for x in inF:
    tempStr = ''
    tempStr = x.rstrip('/?expref=next-blog')
    tempStr = tempStr + '/feeds/posts/default'
    urls.append(tempStr)
    print(tempStr)

urlClean = set(urls)

for x in urls:
    print(x, file=open("unmodifiedURLList.txt", "a+"))

for x in urlClean:
    print(x, file=open("feedlist.txt", "a+"))