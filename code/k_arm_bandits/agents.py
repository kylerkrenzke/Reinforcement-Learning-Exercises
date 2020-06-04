import random
import math

class BanditAgent:
    def __init__(self, bandit):
        self.bandit = bandit
        self.Q = [0 for i in range(bandit.k)]
        
    def alpha(self, **kwargs):
        raise NotImplementedError
        
    def step(self):
        raise NotImplementedError

class ConstAlphaBanditAgent(BanditAgent):
    def __init__(self, bandit, alpha, epsilon):
        super().__init__(bandit)
        self.alphaval = alpha
        self.epsilon = epsilon
        
    def alpha(self):
        return self.alphaval
        
    def step(self):
        def select_action():
            ret = random.uniform(0,1)
            if ret < self.epsilon:
                return random.randint(0,self.bandit.k-1)
            else:
                return self.Q.index(max(self.Q))
                
        a = select_action()
        r = self.bandit.R(a)
        self.Q[a] += self.alpha() * (r - self.Q[a])
        return r

class EGreedyBanditAgent(BanditAgent):
    def __init__(self, bandit, epsilon):
        super().__init__(bandit)
        self.epsilon = epsilon
        self.N = [0 for i in range(bandit.k)]
        
    def alpha(self, a):
        return (1 / self.N[a])
        
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
        self.Q[a] += self.alpha(a) * (r - self.Q[a])
        return r
        
class UCBGreedyBanditAgent(BanditAgent):
    def __init__(self, bandit, c):
        super().__init__(bandit)
        self.N = [0 for i in range(bandit.k)]
        self.c = c
        self.t = 0
        
    def alpha(self, a):
        return (1 / self.N[a])
        
    def step(self):
        def select_action():
            for i in range(len(self.N)):
                if self.N[i] == 0:
                    return i
            ucbq = [self.Q[i] + self.c * sqrt(log(self.t)/self.N[i]) for i in range(self.bandit.k)]
            return ucbq.index(max(self.ucbq))
        
        self.t += 1
        a = select_action()
        r = self.bandit.R(a)
        self.N[a] += 1
        self.Q[a] += self.alpha(a) * (r - self.Q[a])