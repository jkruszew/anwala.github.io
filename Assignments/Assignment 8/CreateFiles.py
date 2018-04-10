for x in range(10):
    print("", file=open("/home/jonathan/PycharmProjects/Assignment8/Testing/Spam"+str(x)+".txt", "w"))
    print("", file=open("/home/jonathan/PycharmProjects/Assignment8/Testing/NotSpam"+str(x)+".txt","w"))
    print("", file=open("/home/jonathan/PycharmProjects/Assignment8/Training/Spam"+str(x)+".txt", "w"))
    print("", file=open("/home/jonathan/PycharmProjects/Assignment8/Training/NotSpam" + str(x) + ".txt", "w"))

