def policy_evaluation(pi, S, A, theta):
    V = [0 for i in range(len(S))]
    
    delta = 0
    while delta > theta:
        for s in S:
            v = V[s]
            # update V[s]
            delta = max(delta, abs(v - V[s]))