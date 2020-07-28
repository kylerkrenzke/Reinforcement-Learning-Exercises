import random

class KBandit:
    def __init__(self, k, Q=None):
        self.k = k
        self.Q = Q or [random.gauss(0,1) for i in range(k)]

    def R(self, a):
        return random.gauss(self.Q[a], 1)
        
class KBanditDynamic(KBandit):
    def __init__(self, k, Q=None):
        super().__init__(k, Q or [0 for i in range(k)])
        
    def step(self):
        for i in range(self.k):
            self.Q[i] += random.gauss(0, 0.1)

