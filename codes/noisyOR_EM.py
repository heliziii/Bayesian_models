import math
n = 23
p = [0.05 for i in range(n)]
iterations = 257

X = []
Y = []
with open("noisyOrX.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(" ")
        line = [int(x) for x in line]
        X.append(line)

with open("noisyOrY.txt") as f:
    for line in f:
        line = line.strip()
        Y.append(int(line))


def e_step(y, X, p, i):
    if (X[i] == 0) or (y == 0):
        return 0
    mult = 1
    for index in range(n):
        mult *= (1-p[index])**X[index]
    return (y*p[i]*X[i]) / (1 - mult)


def update_p(p,i):
    sum = 0
    T_i = 0
    for k in range(len(X)):
        posterior = e_step(Y[k],X[k],p,i)
        sum += posterior
        if X[k][i] == 1:
            T_i += 1
    return sum/T_i


def calc_log(p):
    incorrect = 0
    sum = 0
    for k in range(len(Y)):
        mult = 1
        for i in range(n):
            mult *= (1 - p[i])**X[k][i]
        P_1 = 1 - mult
        P_0 = mult
        P = 0
        if Y[k] == 1:
            P = P_1
        else:
            P = P_0
        if (P_1 > 0.5) and (Y[k] == 0):
            incorrect += 1
        elif (P_1 < 0.5) and (Y[k] == 1):
            incorrect += 1
        sum += math.log(P)
    return incorrect, sum/len(X)


for it in range(iterations):
    print(it)
    print(calc_log(p))
    new_p = []
    for i in range(n):
        new_p.append(update_p(p,i))
    p = new_p




