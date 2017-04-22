# work in progress
def isPalandrome(sNum):
    if(len(sNum) <= 1):
        return True
    f = sNum[:1]
    l = sNum[len(sNum)-1:]
    if(f != l):
        return False
    else:
        return isPalandrome(sNum[1:len(sNum)-1])

def findHighestPal(lowNum, highNum):
    found = False
    answer = 0
    for i in range(lowNum, highNum):
        for j in range(lowNum, highNum):
            numToTest = i*j
            sNumToTest = str(numToTest)
            if(isPalandrome(sNumToTest) and numToTest > answer):
                answer = numToTest
    return answer


print(findHighestPal(100, 1000))

