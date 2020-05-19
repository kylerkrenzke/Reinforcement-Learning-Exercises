import random
import matplotlib.pyplot as plt

class KBandit:
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
        
    def opt_action(self, lst):
        i,opta = 0,0
        cur = lst[0]
        for val in lst:
            if val > cur:
                opta = i
            i += 1
        return opta
    
class KBanditDynamic(KBandit):
    def __init__(self, k, epsilon, rewards=None):
        super().__init__(k, epsilon, rewards=[(0,1) for i in range(k)])
        
    def step(self):
        def select_action():
            ret = random.uniform(0,1)
            if ret < self.epsilon:
                return random.randint(0, len(self.Q)-1)
            else:
                return self.Q.index(max(self.Q))
        for mu,sigma in self.rewards:
            mu += random.gauss(0, 0.01)

        a = select_action()
        r = self.R(a)
        self.N[a] += 1
        self.Q[a] += self.alpha(a) * (self.R(a) - self.Q[a])
        return (self.opt_action([mu for mu,sigma in self.rewards]), a, self.Q[a])

########## for exercise 2.5 ##########
n_mab = 2000
n_step = 10000
mabset = [KBanditDynamic(10, 0.1) for i in range(n_mab)]

avgr, opta = [], []
for i in range(n_step):
    data = []
    for mab in mabset:
        data.append(mab.step())
    rsum, optcnt = 0, 0
    for x in data:
        rsum +=  x[2]
        optcnt += 1 if x[0] == x[1] else 0
    avgr.append(rsum/n_mab)
    opta.append(optcnt/n_mab)

steps = [i for i in range(n_step)]
plt.plot(steps, avgr)
plt.show()

plt.plot(steps, opta)
plt.show()
