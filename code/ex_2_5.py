import matplotlib.pyplot as plt

from kbandit import *
from bandit_agents import *

nbandits = 2000
k = 10
nsteps = 10000

bandits = [KBanditDynamic(k) for i in range(nbandits)]
sampleagents = [SampleAvgAgent(bandits[i], 0.1) for i in range(nbandits)]
constagents = [ConstantStepAgent(bandits[i], 0.1) for i in range(nbandits)]

samplerewards = [0 for i in range(nsteps)]
constrewards = [0 for i in range(nsteps)]
for i in range(nsteps):
    for agent in sampleagents:
        samplerewards[i] += agent.step()
    samplerewards[i] /= nbandits
        
    for agent in constagents:
        constrewards[i] += agent.step()
    constrewards[i] /= nbandits
        
    for bandit in bandits:
        bandit.step()
        
x1 = [i for i in range(nsteps)]
y1 = samplerewards
y2 = constrewards

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.legend(["Sample Average", "Constant Step Size"])
plt.show()