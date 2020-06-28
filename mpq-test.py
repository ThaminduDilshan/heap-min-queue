from mpq import *

print "-----------------------------A-----------------------------"
A=["Empty",2,5,3,86,12,6,3,7,97,100]
print A
print "MPQ :",MPQCreate(A)
print "Enqueue 1:",MPQEnqueue(A,1)
print "Enqueue 120:",MPQEnqueue(A,120)
print "Dequeue :",MPQDequeue(A)
print "After Dequeue :",A
print "Increase 5->120 :",MPQIncreasePriority(A,5,120)
print "Decrease 1->12 :",MPQDecreasePriority(A,1,12)
