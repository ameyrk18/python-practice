import time
from random import  randrange

def findmin(alist):
    overallmin=alist[0]
    for i in alist:
        issmallest=True
        for j in alist:
            if i>j:
                issmallest=False
        if issmallest:
            overallmin=i
    return overallmin

#print(findmin(alist=[5,4,2,1,0]))
#print(findmin(alist=[0,4,2,1,5]))

'''
def findmin(alist):
    minsofar=alist[0]
'''


for listsize in range(1000,10001,1000):
    alist=[randrange(100000) for x in range(listsize)]
    #print(alist)
    start=time.time()
    print(findmin(alist))
    end=time.time()
    print("Size: %d time: %f" %(listsize,end-start))
