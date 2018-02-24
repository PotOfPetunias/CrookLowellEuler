# Find the fisrt triangle number that has more that 500 factors
from EulerUtilities import numOfFactors

triNum = 1
for i in range(2, 10**6):
    triNum += i
    nFac = numOfFactors(triNum)
    if nFac > 500:
        print(triNum)
        break
