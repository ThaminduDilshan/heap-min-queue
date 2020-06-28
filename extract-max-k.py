from heap import *

def ExtractMaxK(NumberList, k):
    if(NumberList[0]!='Empty'):
        tempList = ['Empty'] + NumberList
    else:
        tempList = NumberList

    output = []
    tempList = HeapBuildMaxHeap(tempList)
    for i in range(0,k,1):
        output.append( HeapExtractMax(tempList) )

    return output
    
        
##    largest = tempList[1]
##    heap_size = len(tempList)
##    l = HeapLeft(i)
##    r = HeapRight(i)
##    if (l <= heap_size and A[l] > A[i]):
##        largest = l
##    if (r <= heap_size and A[r] > A[largest]):
##        largest = r
##    
##    if(largest != i):
##        (A[i], A[largest]) = (A[largest], A[i])
##        HeapMaxHeapify(A, largest)
##  return A


#print ExtractMaxK([1,2,6,3,78],3)
#print ExtractMaxK(['Empty',1,2,6,3,78],4)
#print ExtractMaxK([45,3,2,78,34,12,78,9,45,34,567,876,12,2],5)
