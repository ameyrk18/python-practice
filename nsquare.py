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

print(findmin(alist=[5,4,2,1,0]))
