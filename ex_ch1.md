# Chapter 1 Exercises

## Exercise 1.1
### Suppose, instead of playing against a random opponent, the reinforcement learning algorithm described above played
### against itself, with both sides learning. What do you think would happen in this case? Would it learn a different
### policy for selecting moves?

Yes, it would learn a different policy for selecting moves. The values of all the squares would change over time as
the opponent changes their strategy.

Exercise 1.2: Many tic-tac-toe positions appear different but are really the same because of symmetries. How might we
amend the learning process described above to take advantage of this? In what ways would this change improve the
learning process? Now think again. Suppose the opponent did not take advantage of symmetries. In that case, should we?
Is it true, then, that symmetrically equivalent positions should necessarily have the same value?

The learning process could be amended to identify states as the same if they are symmetrically identical. This could
improve the learning process by requiring less total states to converge. However, if the opponent plays differently on
two different, yet symmetric boards, the agent is short-changing its state space and will not find the optimal
solution.

Exercise 1.3: Suppose the reinforcement learning player was greedy, that is, it always played the move that brought it
to the position that it rated the best. Might it learn to play better, or worse, than a nongreedy player? What problems
might occur?