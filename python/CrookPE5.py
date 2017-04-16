
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
print(answer)
