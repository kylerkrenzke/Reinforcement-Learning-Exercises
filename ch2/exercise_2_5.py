import matplotlib.pyplot as plt

from k_arm_bandit import KBanditDynamic

k = 10
nbandits = 2000
epsilon = 0.1
nsteps = 10000

savg_bandits = [KBanditDynamic(k, epsilon)                     for i in range(nbandits)]
cnst_bandits = [KBanditDynamic(k, epsilon, alpha=lambda a:0.1) for i in range(nbandits)]

x = [i for i in range(nsteps)]
savg_avg_r, cnst_avg_r = [0 for i in range(nsteps)], [0 for i in range(nsteps)]
savg_opt_a, cnst_opt_a = [0 for i in range(nsteps)], [0 for i in range(nsteps)]
for i in range(nsteps):
    for bandit in savg_bandits:
        r,opt = bandit.step()
        savg_avg_r[i] += r   # add current bandits reward
        savg_opt_a[i] += opt # add current bandits optimal action hit/miss result
        
    for bandit in cnst_bandits:
        r,opt = bandit.step()
        cnst_avg_r[i] += r   # add current bandits reward
        cnst_opt_a[i] += opt # add current bandits optimal action hit/miss result
    
    savg_avg_r[i] /= nbandits # sample average step size's average reward
    cnst_avg_r[i] /= nbandits # constant step-size's average reward
    
    savg_opt_a[i] /= nbandits # get the sample average step size's average optimal action percentage
    cnst_opt_a[i] /= nbandits # get the constant step-size's average optimal action percentage
        
plt.plot(x, savg_avg_r)
plt.plot(x, cnst_avg_r)
plt.legend(["Sample Average", "Constant Step Size"])
plt.show()

plt.plot(x, savg_opt_a)
plt.plot(x, cnst_opt_a)
plt.legend(["Sample Average", "Constant Step Size"])
plt.show()