from random import random
def getS(com, mine):
    ret = 0
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]

    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    if c1 == m1 :
        ret += 1
    if c2 == m2 :
        ret += 1
    if c3 == m3 :
        ret += 1
    
    return ret

def getB(com, mine):
    ret = 0
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]

    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    if c1 == m2 or c1 == m3 :
        ret += 1
    if c2 == m1 or c2 == m3 :
        ret += 1
    if c3 == m1 or c3 == m2 :
        ret += 1
    
    return ret

def ranC():
    arr = ["1","2","3","4","5","6","7","8","9"]
    
    for i in range(100):
        rnd = int(random()*9)
        a = arr[0]
        arr[0] = arr[rnd]
        arr[rnd] = a
        
    ret = arr[0] + arr[1] + arr[2]    
    print("ret",ret)
    return ret

com = ranC()

while True:
    mine = input("세 숫자를 넣으세요 ")
    s = getS(com,mine)
    b = getB(com,mine)
    print(mine,"\t",s,"s",b,"b")
    
    if s == 3:
        print(mine+"를 맞췄습니다.")
        break

