def isPalandrome(sNum):
    if(len(sNum) <= 1):
        return True
    f = sNum[:1]
    l = sNum[len(sNum)-1:]
    if(f != l):
        return False
    else:
        return isPalandrome(sNum[1:len(sNum)-1])


maxNum = 999

for i in range(maxNum):
    num = str(maxNum*(maxNum-i))
    if(isPalandrome(num)):
        print(num)
        break
