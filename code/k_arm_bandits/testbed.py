from bandits import KBandit
from agents import EGreedyBanditAgent, ConstAlphaBanditAgent, UCBGreedyBanditAgent

import matplotlib.pyplot as plt

def run(nbandits, nsteps):
    # initialize agents
    agents0 = []
    agents01 = []
    agents001 = []
    for i in range(nbandits):
        agents0.append(EGreedyBanditAgent(KBandit(10), 0))
        agents01.append(EGreedyBanditAgent(KBandit(10), 0.1))
        agents001.append(EGreedyBanditAgent(KBandit(10), 0.01))
        
    avgr0, avgr01, avgr001 = [], [], []
    for i in range(nsteps):
        r0, r01, r001 = 0, 0, 0
        for j in range(nbandits):
            r0 += agents0[j].step()
            r01 += agents01[j].step()
            r001 += agents001[j].step()
        avgr0.append(r0/nbandits)
        avgr01.append(r01/nbandits)
        avgr001.append(r001/nbandits)
        
    x = [i for i in range(nsteps)]
    plt.plot(x, avgr0)
    plt.plot(x, avgr01)
    plt.plot(x, avgr001)
    plt.legend(["e=0","e=0.1","e=0.01"])
    plt.show()

bandit = UCBGreedyBanditAgent(KBandit(10), 2)
bandit.step()