



## Well actually it is not quite a binary tree :(
##triagle = [0,3,7,4,2,4,6,8,5,9,3]
##
##cNode = 1
##
##def getleft():
##    global cNode
##    return cNode*2
##def getright():
##    global cNode
##    return cNode*2+1
##def moveleft():
##    global cNode
##    cNode = cNode*2
##def moveright():
##    global cNode
##    cNode = cNode*2+1
##
##def greedy():
##    global cNode
##    global triangle
##    tempCN = cNode
##    cNode = 1
##    s = 0
##    while cNode*2+1 <= len(triangle):
##        s += trangle[cNode]
##        dif = triangle[getleft()] - triangle[getright()]
##        if dif > 0:
##            moveleft()
##        else:
##            moveright()
##    s += trangle[cNode]
##    
