import random
import matplotlib.pyplot as plt

class KBandit:
    def __init__(self, k, epsilon, alpha=None, rewards=None):
        self.Q = [0 for i in range(k)]
        self.N = [0 for i in range(k)]
        self.epsilon = epsilon
        
        if alpha == None:
            self.alpha = lambda a: 1/self.N[a] # default to sample average
        else:
            self.alpha = alpha
        
        if rewards == None:
            self.rewards = [(random.gauss(0,1), 1) for i in range(k)] # default to random rewards Gauss(0,1)
        else:
            self.rewards = rewards
        
    def R(self, a):
        return random.gauss(self.rewards[a][0], self.rewards[a][1])
        
    def step(self):
        def select_action():
            ret = random.uniform(0,1)
            if ret < self.epsilon:
                return random.randint(0, len(self.Q)-1)
            else:
                return self.Q.index(max(self.Q))

        a = select_action()
        r = self.R(a)
        self.N[a] += 1
        self.Q[a] += self.alpha(a) * (self.R(a) - self.Q[a])
        
    def opt_action(self, lst):
        i,opta = 0,0
        cur = lst[0]
        for val in lst:
            if val > cur:
                opta = i
            i += 1
        return opta
    
class KBanditDynamic(KBandit):
    def __init__(self, k, epsilon, alpha=None, rewards=None):
        super().__init__(k, epsilon, alpha=alpha, rewards=[(0,1) for i in range(k)])
        
    def step(self):
        def select_action():
            ret = random.uniform(0,1)
            if ret < self.epsilon:
                return random.randint(0, len(self.Q)-1)
            else:
                return self.Q.index(max(self.Q))
        
        # dynamically modify rewards
        for mu,sigma in self.rewards:
            mu += random.gauss(0, 0.01)

        a = select_action()
        r = self.R(a)
        self.N[a] += 1
        self.Q[a] += self.alpha(a) * (self.R(a) - self.Q[a])
        return max(self.Q), 1 if a==self.opt_action(self.Q) else 0
