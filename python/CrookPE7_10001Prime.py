#Find the 10,001st prime number

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
        


primes = []
underNum = 1000
while len(primes) < 10001:
    primes = primesUnder(underNum)
    underNum += 10000
    print(underNum)

print('Answer: ', primes[10000])
