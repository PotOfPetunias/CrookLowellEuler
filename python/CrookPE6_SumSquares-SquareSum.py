#Find the difference between the sum of the squares of the
#first one hundred natural numbers and the square of the sum.

sum1 = sum([i**2 for i in range(1,101)])
sum2 = (sum([i for i in range(1,101)]))**2
print(sum2-sum1)
