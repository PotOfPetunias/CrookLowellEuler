import math

def nCr(n,r):
    top = 1
    bottom = 1
    if n - r > r:
        r = n - r
    for i in range(r,n):
        top *= i+1
    for i in range(n - r):
        bottom *= i+1
    return int(top / bottom)

def numOfFactors(n):
    pFac = findPrimeFactors(n)
    total = 1
    last = pFac[0]
    count = 0
    for num in pFac:
        if num == last:
            count += 1
        else:
            total *= count + 1
            count = 1
        last = num
    total *= count + 1
    return total

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

def findPrimeFactors(num):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    if i == num:
        return [int(num)]
    else:
        factorList = [i]
        factorList.extend(findPrimeFactors(num/i))
        return factorList

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
