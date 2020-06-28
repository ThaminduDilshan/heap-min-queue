def HeapParent(i):
  return i/2

def HeapLeft(i):
  return 2*i

def HeapRight(i):
  return 2*i + 1

def HeapMax(A):
  return A[1]

def HeapMaxHeapify(A, i):
  largest = i
  heap_size = len(A)-1
  l = HeapLeft(i)
  r = HeapRight(i)
  if (l <= heap_size and A[l] > A[i]):
    largest = l
  if (r <= heap_size and A[r] > A[largest]):
    largest = r
    
  if(largest != i):
    (A[i], A[largest]) = (A[largest], A[i])
    HeapMaxHeapify(A, largest)
  return A

def HeapBuildMaxHeap(A):
  heap_size = len(A)-1
  for i in range(heap_size/2, 0, -1):
    HeapMaxHeapify(A, i)
  return A

def HeapExtractMax(A):
    if( len(A)==2 ):
        return A.pop()
    if( len(A)>2 ):
        max_val = A[1]
        A[1] = A.pop()
        HeapBuildMaxHeap(A)
        return max_val
  
def HeapIncreaseKey(A, i, key):
    if( i<len(A) and i>0):
        A[i] = key
        HeapBuildMaxHeap(A)
    
        return A

def HeapMaxHeapInsert (A, key):
  A.append(key)
  return HeapBuildMaxHeap(A)
  
