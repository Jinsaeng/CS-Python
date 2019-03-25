##import time
##import random
##class PolyTimer:
##    def __init__(self):
##        self.start = time.time()
##
##    def elapsed(self):
##        return time.time() - self.start
##
##    def reset(self):
##        self.start = time.time()
##        
##def maxSubsequenceSum3(vals):
##    n = len(vals)
##    thisSum = 0
##    maxSum = 0
##    
##    i = 0
##    seqStart = 0
##    seqEnd = 0
##    for j in range(n):
##        thisSum += vals[j]
##        if (thisSum > maxSum):
##            maxSum = thisSum
##            seqStart = i
##            seqEnd = j
##        elif (thisSum < 0):
##            i = j + 1
##            thisSum = 0
##
##    return maxSum, seqStart, seqEnd
##def maxSubsequenceSum2(vals):
##    n = len(vals)
##    maxSum = 0
##    seqStart = 0
##    seqEnd = 0
##
##    for i in range(n):
##        thisSum = 0
##        for j in range(i, n):
##            thisSum += vals[j]
##            if (thisSum > maxSum):
##                maxSum = thisSum
##                seqStart = i
##                seqEnd = j
##
##    return maxSum, seqStart, seqEnd
##def maxSubsequenceSum1(vals):
##    n = len(vals)
##    maxSum = 0
##    seqStart = 0
##    seqEnd = 0
##
##    for i in range(n):
##        for j in range(i, n):
##            thisSum = 0
##            for k in range(i, j + 1):
##                thisSum += vals[k]
##            if (thisSum > maxSum):
##                maxSum = thisSum
##                seqStart = i
##                seqEnd = j
##
##    return maxSum, seqStart, seqEnd
##
##
##def main():
##    for n in range(7,13):
##        t = PolyTimer()
##        nuClicks = 0.0
##        someList = []
##        for ele in range(2**n):
##            someList.append(random.randint(-1000,1000))
##        t.reset()
##        #result3, start3, end3 = maxSubsequenceSum3(someList)
##        #result2, start2, end2 = maxSubsequenceSum2(someList)
##        #result1,start1,end1 = maxSubsequenceSum1(someList)
##        nuClicks = t.elapsed()
##        print(nuClicks)
##main()
import random
def move_zeroes(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.remove(lst[i])
            lst.append(0)
    return lst
def main():
    lst = []
    for i in range(100):
        lst.append(random.randint(0,100))
    print(move_zeroes(lst))
    
main()

