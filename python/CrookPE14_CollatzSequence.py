# very slow but it shows the answer eventualy

def colSeq(num):
    seq = [num]
    while seq[-1] != 1:
        if seq[-1] % 2 == 0:
            seq.append(int(seq[-1]/2))
        else:
            seq.append(3*seq[-1] + 1)
    return seq

besti = 0
bestn = 0
for i in range(872,1000001):
    n = len(colSeq(i))
    if n > bestn:
        bestn = n
        besti = i
        print(besti, bestn)
