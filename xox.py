from random import randint

VARS = 19683
V = [0] * VARS
rm = [0] * 10
m = [0] * 10
steps_m = [0] * 10
A = 0.95
steps = 0

def getV(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    num = ((((((((a1*3)+a2)*3+a3)*3+b1)*3+b2)*3+b3)*3+c1)*3+c2)*3+c3
    return V[num]

def setV(a1, a2, a3, b1, b2, b3, c1, c2, c3, v):
    global V
    num = ((((((((a1*3)+a2)*3+a3)*3+b1)*3+b2)*3+b3)*3+c1)*3+c2)*3+c3
    V[num] = v

def readMap(st):
    global rm
    for i in range(9, 0, -1):
        rm[i] = st % 3
        st //= 3

def printMap():
    for i in range(1, 10):
        if (i - 1) % 3 == 0:
            print('|', sep='', end='')
        if m[i] == 1:
            print('X', sep='', end='|')
        elif m[i] == 2:
            print('O', sep='', end='|')
        else:
            print(i, sep='', end='|')
        if i % 3 == 0:
            print()

def learnAI(res):
    global V, A, steps_m
    for i in range(steps):
        V[steps_m[i]] += A * (res - V[steps_m[i]])
    A -= 0.01

def checkEnd():
    if m[1]==m[2] and m[2]==m[3]:
        return m[1]
    if m[4]==m[5] and m[5]==m[6]:
        return m[4]
    if m[7]==m[8] and m[8]==m[9]:
        return m[7]
    if m[1]==m[4] and m[4]==m[7]:
        return m[1]
    if m[2]==m[5] and m[5]==m[8]:
        return m[2]
    if m[3]==m[6] and m[6]==m[9]:
        return m[3]
    if m[1]==m[5] and m[5]==m[9]:
        return m[1]
    if m[7]==m[5] and m[5]==m[3]:
        return m[7]

    return 0

def stepAI():
    global VARS, steps, steps_m, m
    var = [0] * 10
    c_var = 0
    for i in range(VARS):
        flag = 0
        readMap(i)
        for j in range(1, 10):
            if rm[j] != m[j]:
                if m[j] == 0 and rm[j] == 1:
                    flag += 1
                else:
                    flag += 2
                if flag > 1:
                    break
        if flag == 1:
            var[c_var] = i
            c_var += 1

    if randint(0, 100) < 5:
        v_num_max = randint(0, c_var)
    else:
        v_max = V[var[0]]
        v_num_max = 0
        if c_var > 1:
            for i in range(1, c_var):
                if V[var[i]] > v_max:
                    v_num_max = i

    steps += 1
    steps_m[steps] = var[v_num_max]
    
    readMap(var[v_num_max])
    for i in range(1, 10):
        m[i] = rm[i]

    printMap()

def initV():
    for a1 in range(3):
        for a2 in range(3):
            for a3 in range(3):
                for b1 in range(3):
                    for b2 in range(3):
                        for b3 in range(3):
                            for c1 in range(3):
                                for c2 in range(3):
                                    for c3 in range(3):
                                        setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,0.5)

                                        if a1==a2 and a2==a3 and a1 != 0:
                                            v = a1 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)
                                        if b1==b2 and b2==b3 and b1 != 0:
                                            v = b1 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)
                                        if c1==c2 and c2==c3 and c1 != 0:
                                            v = c1 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)
                                        if a1==b2 and b2==c3 and a1 != 0:
                                            v = a1 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)
                                        if a3==b2 and b2==c1 and a3 != 0:
                                            v = a3 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)
                                        if a1==b1 and b1==c1 and a1 != 0:
                                            v = a1 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)
                                        if a2==b2 and b2==c2 and a2 != 0:
                                            v = a2 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)
                                        if a3==b3 and b3==c3 and a3 != 0:
                                            v = a3 % 2
                                            setV(a1,a2,a3,b1,b2,b3,c1,c2,c3,v)

def user_step(xo_num):
    global m
    if m[xo_num] == 0:
        m[xo_num] = 2
    else:
        return False
    return True

def next_step(end):
    if not end:
        stepAI()
    if checkEnd() == 1:
        print("Win PC")
        learnAI(1)
        new_game()
    elif checkEnd() == 2:
        print("You win")
        learnAI(0)
        new_game()
    if steps == 5:
        learnAI(0)
        new_game()

    print("Your step: ")
    while not user_step(int(input())):
        print("Try again:")
    next_step(checkEnd())

def new_game():
    global steps, end, m
    steps = 0
    end = 0
    for i in range(1, 10):
        m[i] = 0
    print("NEW GAME")
    next_step(0)

def init():
    global A
    A = 0.95
    initV()
    new_game()

if __name__ == "__main__":
    init()
    
