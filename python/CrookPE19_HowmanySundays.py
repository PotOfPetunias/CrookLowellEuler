import itertools as itr

wlist = [i for i in range(1,8)]
mDeeplist = [[i for i in range(31)],
             [i for i in range(28)],
             [i for i in range(31)],
             [i for i in range(30)],
             [i for i in range(31)],
             [i for i in range(30)],
             [i for i in range(31)],
             [i for i in range(31)],
             [i for i in range(30)],
             [i for i in range(31)],
             [i for i in range(30)],
             [i for i in range(30)]]
mDeepLeeplist = [[i for i in range(31)],
                 [i for i in range(29)],
                 [i for i in range(31)],
                 [i for i in range(30)],
                 [i for i in range(31)],
                 [i for i in range(30)],
                 [i for i in range(31)],
                 [i for i in range(31)],
                 [i for i in range(30)],
                 [i for i in range(31)],
                 [i for i in range(30)],
                 [i for i in range(30)]]

mlist = [item for sublist in mDeeplist for item in sublist]
mllist = [item for sublist in mDeepLeeplist for item in sublist]
print(len(mlist))
print(len(mllist))
weekIter = itr.cycle(wlist)
monthIter = itr.cycle(mlist)
monthlIter = itr.cycle(mllist)

count = 0
for year in range(1900, 2001):
    if (year % 4 == 0) and year != 1900:
        for day in range(366):
            if weekIter.__next__() == 7:
                if monthlIter.__next__() == 0:
                    count += 1
                    print(year, day, "First of month and sunday")
            else:
                monthlIter.__next__()
    else:
        for day in range(365):
            if weekIter.__next__() == 7:
                if monthIter.__next__() == 0:
                    count += 1
                    
            else:
                monthIter.__next__()
print(count)
