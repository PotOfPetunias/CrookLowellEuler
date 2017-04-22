# work in progress
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

def findSmallDivisible(numList):
    primeFactors = []
    for num in numList:
        if num == 0 or num == 1:
            continue
        primeFactors.extend(findPrimeFactors(num))
    #primeFactors = list(set(primeFactors))
    answer = 1
    for num in primeFactors:
        answer = answer*num
    return answer

print(findSmallDivisible([i for i in range(0,11)]))
'''
num = 2*3*5*7*11*13*17*19*2*2*3*5
answer = num
adding = 1
for i in range(1,21):
    if (num % i)!= 0:
        print(num % i, " ", i)
        if (adding % i)!= 0:
            adding = adding*(num % i)
print(answer)

num = 2*3*5*7
answer = num
for i in range(1,11):
    if (num % i)!= 0:
        print(num % i, " ", i)
        answer = answer*(num % i)
print(answer)'''
