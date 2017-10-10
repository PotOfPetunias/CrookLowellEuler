import math
def primesUnder(num):
    integerList = [i for i in range(num+1)]
    markList = [False for i in range(num+1)]
    for i in range(2,int(math.ceil(math.sqrt(num+1)))):
        if not markList[i]:
            print('Marking every ', i)
            for j in range(i*2,num+1,i):
                if not markList[j]:
                    #print('Marking ', integerList[j])
                    markList[j] = True
                
    for i in reversed(range(len(markList))):
        if markList[i]:
            del integerList[i]
            
    return integerList[2:]

print(sum(primesUnder(2000000)))
