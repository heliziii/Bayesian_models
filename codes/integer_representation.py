import random
import matplotlib.pyplot as plt

def generator(sample,index):
    states = {}
    alpha = 0.1

    for i in range(sample):
        w = 1
        X = []
        f = 0
        for j in range(1, 11):
            X.append(random.randint(0,1))
            f += 2 ** (j - 1) * X[j - 1]
        X.append(128)
        w *= ((1 - alpha) / (1 + alpha)) * (alpha ** abs(128 - f))

        X = tuple(X)
        if X in states:
            states[X] += w
        else:
            states[X] = w

    face, denominator = 0, 0
    for X, w in states.items():
        if X[10] == 128:
            denominator += w
        if X[index - 1] == 1 and X[10] == 128:
            face += w

    return face / denominator



for index in [10]:
    output = []
    for i in range(10000,5000000,500000):
        output.append(generator(i,index))
    print(output)
    plt.scatter(range(10000,5000000,500000),output)
    plt.xlabel("number of samples")
    plt.ylabel("P for index = " + str(index))
    plt.show()
