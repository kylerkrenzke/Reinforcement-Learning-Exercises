import random

class kbandit:
    def __init__(self, k, epsilon, rewards = None):
        self.Q = [0 for i in range(k)]
        self.N = [0 for i in range(k)]
        self.epsilon = epsilon
        
        if rewards == None:
            self.rewards = [(random.gauss(0,1), 1) for i in range(k)]
        else:
            self.rewards = rewards

    def alpha(self, a):
        return 1/self.N[a]
        
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
    
mab10 = kbandit(10, 0.1)

for i in range(2000000):
    mab10.step()

for i in range(10):
    print("q*({}) = {} --> Q({}) = {}".format(i, mab10.rewards[i], i, mab10.Q[i]))
    