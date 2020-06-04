import random

class EGreedyBanditAgent:
    def __init__(self, bandit, epsilon):
        self.bandit = bandit
        self.epsilon = epsilon
        self.Q = [0 for i in range(bandit.k)]
        self.N = [0 for i in range(bandit.k)]
        
    def step(self):
        def select_action():
            ret = random.uniform(0,1)
            if ret < self.epsilon:
                return random.randint(0,self.bandit.k-1)
            else:
                return self.Q.index(max(self.Q))
                
        a = select_action()
        r = self.bandit.R(a)
        self.N[a] += 1
        self.Q[a] += (1 / self.N[a]) * (r - self.Q[a])
        return r