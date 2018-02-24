#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

num = 1000
multOf3 = [i*3 for i in range(int(num/3)+1)]
multOf5 = [i*5 for i in range(int(num/5))]
print(sum(list(set(multOf3+multOf5))))


#one line version just for fun
#print(sum(list(set([i*3 for i in range(int(1000/3)+1)]+[i*5 for i in range(int(1000/5))]))))
