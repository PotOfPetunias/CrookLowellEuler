#Find the thirteen adjacent digits in
#the 1000-digit number that have the greatest product

import math

file = open("Prob8Number.txt")
number = file.readlines()
number = number[0]
file.close()
dlist = []
for d in number:
    dlist.append(int(d))

for d in range(len(dlist)):
    if dlist[d] < 4:
        dlist[d] = 0

mlist = []
for d in range(len(dlist)):
    for i in range(13):
        if dlist[d+i] == 0:
            break
        else:
            mlist.append(dlist[d+i])
    if len(mlist) == 13:
        p = 1
        for i in mlist:
            p *= i
        print(p)
    mlist = []
    
    
