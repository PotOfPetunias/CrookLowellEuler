# Find the largest prime factor of the number 600851475143

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
    
list = findPrimeFactors(600851475143)

for num in list:
    print(num)
