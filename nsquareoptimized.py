import time
from random import  randrange

def findmin(alist):
    minsofar=alist[0]
    for i in alist:
        if i<minsofar:
            minsofar=i
    return minsofar

for listsize in range(1000,10001,1000):
    alist=[randrange(100000) for x in range(listsize)]
    #print(alist)
    start=time.time()
    print(findmin(alist))
    end=time.time()
    print("Size: %d time: %f" %(listsize,end-start))
