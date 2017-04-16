def isPalandrome(sNum):
    if(len(sNum) <= 1):
        return True
    f = sNum[:1]
    l = sNum[len(sNum)-1:]
    if(f != l):
        return False
    else:
        return isPalandrome(sNum[1:len(sNum)-1])

def findHighestPal(num):
    found = False
    answer = 0
    for i in range(num):
        for j in range(num):
            numToTest = str((num-i)*(num-j))
            if(isPalandrome(numToTest) and int(numToTest) > answer):
                answer = int(numToTest)
    return answer


print(findHighestPal(999))



