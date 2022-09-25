"""
This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain, 
and a number of steps num_steps. 
Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""
from random import random

def RunMarkovChain(start,transition_probabilities,num_steps):
    prob_dict = MakeDict(transition_probabilities)
    counter = {}
    for key in prob_dict.keys():
        counter[key] = 0
    counter[start] = 1
    current_state = start
    for i in range(num_steps-1):
        random_num = random()
        for next_state in prob_dict[current_state].keys():
            if random_num <= prob_dict[current_state][next_state]: 
                current_state = next_state
                counter[current_state] += 1
                break

    return counter


def MakeDict(transition_probabilities):
    result = {}
    curr_prob = 0
    for t in transition_probabilities:
        if t[0] not in result.keys():
            result[t[0]]={}
            curr_prob = 0
        curr_prob+=t[2]    
        result[t[0]][t[1]] = curr_prob
        
    return result

start = 'a'
num_steps = 5000
transition_probabilities = \
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
    
print(RunMarkovChain(start,transition_probabilities,num_steps))