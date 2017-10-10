import math
squarelist = [i*i for i in range(1,1000)]
for a in squarelist:
    for b in squarelist:
        c = a + b
        hope1000 = math.sqrt(a) + math.sqrt(b) + math.sqrt(c)
        if hope1000 == 1000:
            for i in squarelist:
                if i == c:
                    print(math.sqrt(a)*math.sqrt(b)*math.sqrt(c))
            
