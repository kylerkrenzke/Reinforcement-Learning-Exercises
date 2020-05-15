# Chapter 2 Exercises
## Exercise 2.1
**In e-greedy action selection, for the case of two actions and e = 0.5, what is the probability that the greedy**
**action is selected?**
0.75

## Exercise 2.2: Bandit example
**Consider a k-armed bandit problem with k = 4 actions, denoted 1, 2, 3, and 4. Consider applying to this problem a**
** bandit algorithm using e-greedy action selection, sample-average action-value estimates, and initial estimates of**
**Q1(a) = 0, for all a. Suppose the initial sequence of actions and rewards is A1 = 1, R1 = -1, A2 = 2, R2 = 1, A3 = **
**2, R3 = -2, A4 = 2, R4 = 2, A5 = 3, R5 = 0. On some of these time steps the e case may have occurred, causing an**
**action to be selected at random. On which time steps did this definitely occur? On which time steps could this**
**possibly have occurred?**
The epsilon case definitely occurred for A4=2 because A2=2 and A3=2 received an average reward of -1 which would be less
than the other initally zero valued states. It should also be noted, however, that any or all of these five actions
could be epsislon cases and they randomly selected the greedy option.

## Exercise 2.3
**In the comparison shown in Figure 2.2, which method will perform best in the long run in terms of cumulative reward**
**and probability of selecting the best action? How much better will it be? Express your answer quantitatively.**
The method utilizing epsilon greedy search with an epsilon value of 0.01 will perform best in the long run in terms of
cumulative reward and probability of selecting the best action because it will converge to a probability of 1-e of
selecting the optimal action. Given that, it is trivial that 1-0.01 > 1-0.1.

## Exercise 2.4
**If the step-size parameters, alpha_n, are not constant, then the estimate Qn is a weighted average of previously**
**received rewards with a weighting different from that given by (2.6). What is the weighting on each prior reward**
**for the general case, analogous to (2.6), in terms of the sequence of step-size parameters?**
PROD(i=1,N)[1-alpha_i] * Q_1 + SUM(i=1,N)[alpha_i * PROD(j=i+1,N)[alpha_j * (1 - alpha_j)] * R_i]

## Exercise 2.5 (programming)
**Design and conduct an experiment to demonstrate the diculties that sample-average methods have for nonstationary**
**problems. Use a modified version of the 10-armed testbed in which all the q\*(a) start out equal and then take**
**independent random walks (say by adding a normally distributed increment with mean 0 and standard deviation 0.01**
**to all the q⇤(a) on each step). Prepare plots like Figure 2.2 for an action-value method using sample averages,**
**incrementally computed, and another action-value method using a constant step-size parameter, ↵ = 0.1. Use " = 0.1**
**and longer runs, say of 10,000 steps.**
Find in karmbandit.py

## Exercise 2.6: Mysterious Spikes
**The results shown in Figure 2.3 should be quite reliable because they are averages over 2000 individual, randomly**
**chosen 10-armed bandit tasks. Why, then, are there oscillations and spikes in the early part of the curve for the**
**optimistic method? In other words, what might make this method perform particularly better or worse, on average,**
**on particular early steps?**
The early oscillations and spikes could be caused by the initial optimism of the agent. In the case that the initial
action values are not selected optimistically, the action values start at zero and slowly decrease their bias towards
the true values. In the case of optimistic initial values, however, the first few trials for each action will have a
much larger effect on the estimated action values causing them to decrease quickly. This lets the agent explore more
freely in the early trials. Since it explore more freely earlier, it also has a higher percentage likelihood to select
the optimal action at an earlier time. Once it starts to converge, the optimistic action percentage drops way down and
the rate of increase becomes more typical.