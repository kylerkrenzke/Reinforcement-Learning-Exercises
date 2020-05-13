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