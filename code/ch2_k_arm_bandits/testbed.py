from bandits import KBanditDynamic
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

def run_ex2_5(nbandits, nsteps):
    bandits = [KBanditDynamic(10) for i in range(nbandits)]                           # init bandit problems
    epsagents = [EGreedyBanditAgent(bandits[i], .1) for i in range(nbandits)]         # init e-greedy bandit agents
    cnstagents = [ConstAlphaBanditAgent(bandits[i], .1, .1) for i in range(nbandits)] # init const alpha bandit agents
    
    rewards1 = []                       #     init rewards 1 returns
    rewards2 = []                       #     init rewards 2 returns
    optacts1 = []                       #     init optimal action 1 returns
    optacts2 = []                       #     init optimal actions 2 returns
    for i in range(nsteps):             # for number of steps
        r1, r2, o1, o2 = 0,0,0,0
        for j in range(nbandits):       #     for bandit1,bandit2 in bandits
            ret1 = epsagents[j].step()  #         step bandit1
            ret2 = cnstagents[j].step() #         step bandit2
            r1 += (ret1[0])             #         append rewards for bandit1 to rewards 1
            r2 += (ret2[0])             #         append rewards for bandit2 to rewards 2
            o1 += (ret1[1])             #
            o2 += (ret2[1])             #
            bandits[j].step()           #
        rewards1.append(r1/nbandits)
        rewards2.append(r2/nbandits)
        optacts1.append(o1/nbandits)
        optacts2.append(o2/nbandits)
        
        
    x = [i for i in range(nsteps)]
    
    plt.plot(x, rewards1)
    plt.plot(x, rewards2)
    plt.legend(["sample average","constant alpha"])
    plt.show()
    
    plt.plot(x, optacts1)
    plt.plot(x, optacts2)
    plt.legend(["sample average","constant alpha"])
    plt.show()

run_ex2_5(10000, 10000)
    
