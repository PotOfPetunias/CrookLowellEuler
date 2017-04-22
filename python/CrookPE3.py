# To be honest I am not exactly sure why this works,
# but as far as I can tell it does work.
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
    
print(findPrimeFactors(600851475143))

