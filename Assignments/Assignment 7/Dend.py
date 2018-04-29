import clusters

name, word, data = clusters.readfile('blogdata1 (copy).txt')
cluster = clusters.hcluster(data)

clusters.printclust(cluster, labels=name)

clusters.drawdendrogram(cluster, name, jpeg='BlogCluster.jpg')