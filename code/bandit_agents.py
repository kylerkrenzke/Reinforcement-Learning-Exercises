import random

class EpsilonGreedyAgent:
    def __init__(self, bandit, epsilon=0.1):
        self.bandit = bandit
        self.Q = [0 for i in range(bandit.k)]
        self.N = [0 for i in range(bandit.k)]
        self.epsilon = epsilon
        
    def alpha(self, a):
        raise NotImplementedError
        
    def step(self):
        def select_action():
            ret = random.uniform(0,1)
            if ret < self.epsilon:
                return random.randint(0, self.bandit.k-1)
            else:
                return self.Q.index(max(self.Q))
        
        a = select_action()
        r = self.bandit.R(a)
        self.N[a] += 1
        self.Q[a] += self.Q[a] + self.alpha(a) * (r - self.Q[a])
        return max(self.Q)
        
class SampleAvgAgent(EpsilonGreedyAgent):
    def __init__(self, bandit, epsilon):
        super().__init__(bandit, epsilon=0.1)
        
    def alpha(self, a):
        return 1/self.N[a]
        
class ConstantStepAgent(EpsilonGreedyAgent):
    def __init__(self, bandit, epsilon=0.1, alpha=0.1):
        super().__init__(bandit, epsilon)
        self.consta = alpha
        
    def alpha(self, a):
        return self.consta