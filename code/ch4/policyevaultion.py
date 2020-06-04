def policy_evaluation(S, pi, theta=0.1):
    V = [0 for i in range(len(S))]

    delta = 0
    while delta > theta:
        for i in range(len(S)):
            v = V[i]
            