num = 1000
multOf3 = [i*3 for i in range(int(num/3)+1)]
multOf5 = [i*5 for i in range(int(num/5))]
print(sum(list(set(multOf3+multOf5))))
