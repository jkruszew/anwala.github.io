tp = 0
tn = 0
fp = 0
fn = 0
count = 0
with open('output.txt') as inp:
    for x in inp:
        temp = (x.rstrip('\n')).split(' ')
        if temp[0] == temp[5] and temp[0] =='Spam':
            print(count,": True Negative")
            tn = tn + 1
            print("True Neg: ",tn)
        elif temp[0] == temp[5] and temp[0] =='Not_Spam':
            print(count,": True Positive")
            tp = tp + 1
            print("True Pos: ",tp)
        elif temp[0] != temp[5] and temp[0] =='Spam':
            print(count,": False Positive")
            fp = fp + 1
            print("False Pos: ",fp)
        elif temp[0] != temp[5] and temp[0] =='Not_Spam':
            print(count,": False Negative")
            fn = fn + 1
            print("False Neg: ",fn)
        count = count + 1

precision = float(tp) / float(tp+fp)
recall = float(tp) / float(tp+fn)

print("       Neg Pos")
print("True:  ",tn, " ", tp)
print("False: ",fn, ' ', fp)
print()
print("Precision: ", precision)
print("Recall: ", recall)


print("       Neg Pos", file=open("output2.txt", 'a+'))
print("True:  ",tn, " ", tp, file=open("output2.txt", 'a+'))
print("False: ",fn, ' ', fp, file=open("output2.txt", 'a+'))
print('', file=open("output2.txt", 'a+'))
print("Precision: ", precision, file=open("output2.txt", 'a+'))
print("Recall: ", recall, file=open("output2.txt", 'a+'))