from heap import *

def MPQCreate():
  return []

def MPQCreate(A):
  return HeapBuildMaxHeap(A)

def MPQEnqueue(A, key):
  return HeapMaxHeapInsert(A, key)

def MPQDequeue(A):
  return HeapExtractMax(A)

def MPQIncreasePriority(A, i, newKey):
  if(A[i]<newKey):
    return HeapIncreaseKey(A, i, newKey)

def MPQDecreasePriority(A, i, newKey):
  if(A[i]>newKey):
    if( i<len(A) and i>0):
        A[i] = newKey
        HeapBuildMaxHeap(A)
    
        return A
