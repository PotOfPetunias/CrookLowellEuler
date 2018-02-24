#Find the smallest positive number that is
#evenly divisible by all of the numbers from 1 to 20
from EulerUtilities import findPrimeFactors 
import copy

def findSmallDivisible(numList):
    primeFactors = []
    for num in numList:
        if num == 0 or num == 1:
            continue
        numsFactors = findPrimeFactors(num)
        tempFactorList = copy.copy(primeFactors)
        for i in reversed(range(len(numsFactors))):
            for j in reversed(range(len(tempFactorList))):
                if tempFactorList[j] == numsFactors[i]:
                    del numsFactors[i]
                    del tempFactorList[j]
                    break
        primeFactors.extend(numsFactors)
        #print('num: ', num, '\nFactors We need to add ', numsFactors, '\nNew Factor list ', primeFactors)
        
    answer = 1
    print(primeFactors)
    for num in primeFactors:
        answer = answer*num
    return answer

print(findSmallDivisible([i for i in range(1,21)]))


