#we start with odd even
#odd plus even is odd
#even plus odd is odd
#odd plus odd is even
#repeat... so every third starting with the second is even
maxNum = 4000000
#maxNum = 90
fib = [1,2]
while fib[len(fib)-1] < maxNum:
    fib.append(fib[len(fib)-1]+fib[len(fib)-2])
fib = fib[:len(fib)-1]
print(fib)

i = 1
sum = 0
while i < len(fib):
    sum += fib[i]
    i += 3
print(sum)
