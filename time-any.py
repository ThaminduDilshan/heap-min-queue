from extract-max-k import *
import time
import random

def ExtractTest(NumberList, k):
    begin = time.time()
    ExtractMaxK(NumberList, k)
    end = time.time()
    timeTaken = end - begin
    return timeTaken

def GenerateList(length):
    newList=[]
    for i in range(0,length,1):
        newList.append( random.randrange(0,1000) )
    return newList


##print ExtractTest( GenerateList(10), 5 )
##print ExtractTest( GenerateList(100), 5 )
##print ExtractTest( GenerateList(1000), 5 )
##print ExtractTest( GenerateList(10000), 5 )
##print ExtractTest( GenerateList(100000), 5 )
##print ExtractTest( GenerateList(1000000), 5 )
##print ExtractTest( GenerateList(10000000), 5 )

print ExtractTest( GenerateList(1000000), 5 )
print ExtractTest( GenerateList(2000000), 5 )
print ExtractTest( GenerateList(3000000), 5 )
print ExtractTest( GenerateList(4000000), 5 )
print ExtractTest( GenerateList(5000000), 5 )
print ExtractTest( GenerateList(6000000), 5 )
print ExtractTest( GenerateList(7000000), 5 )
print ExtractTest( GenerateList(8000000), 5 )
print ExtractTest( GenerateList(9000000), 5 )
print ExtractTest( GenerateList(10000000), 5 )
