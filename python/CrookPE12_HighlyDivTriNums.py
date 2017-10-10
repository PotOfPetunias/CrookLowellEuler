import time
import math
def primesUnder(num):
    integerList = [i for i in range(0,num+1)]
    markList = [False for i in range(0,num+1)]

    for i in range(2,int(math.ceil(math.sqrt(num+1)))):
        #print('Marking every ', i)
        for j in range(i*2,num+1,i):
            if not markList[j]:
                #print('Marking ', integerList[j])
                markList[j] = True
                
    for i in reversed(range(len(markList))):
        if markList[i]:
            del integerList[i]
            
    return integerList[2:]

def findFactors(num):
    prms = primesUnder(int(num/2))
    prmfactors = []
    stopped = False
    for n in prms:
        if num % n == 0:
            prmfactors.append(n)
    print(prmfactors)
    
    factors = []
    if len(prmfactors) == 2:
        prmfactors.extend([1,num])
        return prmfactors
    for i in range(len(prmfactors)-1):
        for j in range(i+1, len(prmfactors)):
            factors.append(prmfactors[i]*prmfactors[j])
    factors.extend(prmfactors)
    factors.extend([1,num])
    print(factors)
    factors = list(set(factors))
    factors.sort()
    return factors


start = time.time()
l = findFactors(10005)
end = time.time()
print(l)
print(end-start)


##triNums = [sum([i for i in range(10000)])]
##print(triNums)
##for i in range(10000, 20000):
##    triNums.append(triNums[len(triNums) -1] + i)
##maxNum = 0
##for n in triNums:
##    noFac = len(findAllFactors(n))
##    if noFac > maxNum:
##        maxNum = noFac
##    if maxNum >= 500:
##        print(n)
##        break
##
##print(maxNum)
##test = [i for i in range(1,26)]
##p = 1
##for i in test:
##    p *= i
##print(p)
##print(len(findAllFactors(p)))

