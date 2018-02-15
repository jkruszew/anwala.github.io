tcon = []
with open("MementoAgeList.txt") as inf:
    for x in inf:
        tcon.append(x)

test = [[0 for x in range(2)] for y in range(len(tcon))]
for x in range(len(tcon)):
    mem,b,b2,day = str(tcon[x]).split(' ')
    mem = int(mem)
    day = int(day)

    print(day,' ',mem)
    print(day," ",mem, file=open("AgeMementoList.txt", "a+"))


