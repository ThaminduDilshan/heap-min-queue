from heap import *

print "\n------------------------MyHeap------------------------"
myHeap = ['Empty', 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
print myHeap
HeapMaxHeapify(myHeap, 2)
print "maxHeapify :",myHeap
print HeapExtractMax(myHeap)
print  "ExtractMax :",myHeap
print "insert :", HeapMaxHeapInsert(myHeap,10)

print "\n------------------------MyHeap2------------------------"
myHeap2 = ['Empty', 2, 4, 6, 8, 10, 12, 14, 9, 7, 5, 5, 3, 1]
print myHeap2 
HeapBuildMaxHeap(myHeap2)
print "buildMaxHeap :",myHeap2
print HeapExtractMax(myHeap2)
print  "ExtractMax :",myHeap2
print HeapExtractMax(myHeap2)
print  "ExtractMax :",myHeap2
HeapIncreaseKey(myHeap2, 5, 44)
print "Increase :",myHeap2
print"insert :", HeapMaxHeapInsert(myHeap2,100)

print "\n------------------------MyHeap3------------------------"
myHeap3 = ['Empty',2]
print myHeap3
HeapBuildMaxHeap(myHeap3)
print "buildMaxHeap :",myHeap3 
print HeapExtractMax(myHeap3)
print  "ExtractMax :",myHeap3
print "Increase :",HeapIncreaseKey(myHeap3, 1, 44)
print"insert :", HeapMaxHeapInsert(myHeap3,7)
