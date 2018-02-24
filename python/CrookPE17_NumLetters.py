
nums = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
        11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
        20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6,
        100:10, 1000:11}
numWords = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
            7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',
            12:'twelve', 13:'thirteen', 15:'', 20:'', 30:'', 40:'', 50:'', 60:'', 70:'',
            80:'', 90:'', 100:'', 1000:''}

def getLen(num):
    global nums
    if num in nums:
        return nums[num]
    hplace = num//100
    tens = num % 100
    if tens in nums:
        return nums[tens]+nums[100]+nums[hplace]
    if tens == 0:
        return nums[100]-3+nums[hplace]
    tplace = tens//10
    ones = tens % 10
    if hplace == 0:
        return nums[ones]+nums[tplace*10]
    return nums[ones]+nums[tplace*10]+nums[100]+nums[hplace]
    
s = 0
for i in range(1,1001):
    s += getLen(i)
print(s)



