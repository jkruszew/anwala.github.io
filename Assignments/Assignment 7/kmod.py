import clusters

def printCentroid(name, kcluster, n):
    for x in range(n):
        print("Centroid ", str(x + 1), ":")
        print([name[r] for r in kcluster[x]])
        print("Centroid ", str(x + 1), ":", file=open("kcluster" + str(n) + ".txt", 'a+'))
        print([name[r] for r in kcluster[x]], file=open("kcluster" + str(n) + ".txt", 'a+'))


name, word, data = clusters.readfile('blogdata1 (copy).txt')

kcluster =clusters.kcluster(data,k=5)
printCentroid(name,kcluster,5)

kcluster =clusters.kcluster(data,k=10)
printCentroid(name,kcluster,10)

kcluster =clusters.kcluster(data,k=20)
printCentroid(name,kcluster,20)
