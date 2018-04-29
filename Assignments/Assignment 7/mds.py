import clusters

name, word, data = clusters.readfile('blogdata1 (copy).txt')

cluster = clusters.scaledown(data)

clusters.draw2d(cluster, name, jpeg='mds.jpg')