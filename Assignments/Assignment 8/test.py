import docclass
from subprocess import check_output

cl = docclass.naivebayes(docclass.getwords)
#remove previous db file
#check_output(['rm', 'jkruszew.db'])

cl.setdb('jkruszew.db')
docclass.emailTrain(cl)

for x in range(10):
    email = ''
    with open('/home/jonathan/PycharmProjects/Assignment8/Testing/NotSpam'+str(x)+'.txt') as nSpamIn:
        email = nSpamIn.read()
        print("Not_Spam ",x,": ",cl.classify(email))
        print("Not_Spam ",x,": ",cl.classify(email), file=open('output.txt', 'a+'))

    with open('/home/jonathan/PycharmProjects/Assignment8/Testing/Spam'+str(x)+'.txt') as spamIn:
        email = spamIn.read()
        print("Spam ",x,": ",cl.classify(email))
        print("Spam ",x,": ",cl.classify(email), file=open('output.txt', 'a+'))


#classify text: "the banking dinner" as spam or not spam
#print( cl.classify('the banking dinner') )