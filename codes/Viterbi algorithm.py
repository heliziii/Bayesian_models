import numpy as np
import matplotlib.pyplot as plt
import string


initial = []
emission = [[] for i in range(27)]
transition = [[] for j in range(27)]
observation = ""

with open("initialStateDistribution.txt") as f:
    for line in f:
        initial.append(float(line))

with open("emissionMatrix.txt") as f:
    i = 0
    for line in f:
        em = line.split("\t")
        emission[i].append(float(em[0]))
        emission[i].append(float(em[1]))
        i += 1

with open("transitionMatrix.txt") as f:
    i = 0
    for line in f:
        line = line.strip()
        tr = line.split(" ")
        tr = [np.log(float(k)) for k in tr]
        transition[i] = tr
        i += 1

with open("observations.txt") as f:
    line = f.readline()
    line = line.strip()
    observation = [int(i) for i in line.split(" ")]


l = np.empty((27,len(observation)), dtype=float)
phi = np.empty((27,len(observation)), dtype=float)

initial = np.array(initial)
emission = np.array(emission)
transition = np.array(transition)
l[:,0] = np.log(initial) + np.log(emission[:,observation[0]])


for i in range(1,len(observation)):
    # X = [[0 for ii in range(27)] for jj in range(27)]
    # for ii in range(27):
    #     for jj in range(27):
    #         X[ii][jj] = l[ii][i - 1] + np.math.log(emission[ii][observation[i]])
    # X = np.array(X)
    # l[:, i] = np.max(X + transition.T, 1)
    phi[:, i] = np.argmax(l[:, i - 1] + transition.T, 1)

print("finished filling tabels")
x = np.empty(len(observation),'B')
x[-1] = np.argmax(l[:, len(observation) - 1])
for i in reversed(range(1, len(observation))):
    x[i - 1] = phi[x[i], i]
print(x)

d = {n: ch for n, ch in enumerate(string.ascii_lowercase)}
d[26] = " "
print(d)


plt.scatter([i for i in range(len(observation))],[d[i] for i in x],s = 1 )
plt.show()

