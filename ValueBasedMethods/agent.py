import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.eps = 1.0
        self.epsdecay = 0.999
        self.gamma = 1.0
        self.alpha = 0.01
    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        
        if np.random.random() > self.eps: # select greedy action with probability epsilon
            action= np.argmax(self.Q[state])
        else:                     # otherwise, select an action randomly
            action=np.random.choice(np.arange(self.nA))
        return action
    
    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        current = self.Q[state][action]  # estimate in Q-table (for current state, action pair)
        Qsa_next = np.max(self.Q[next_state]) if next_state is not None else 0  # value of next state 
        target = reward + (self.gamma * Qsa_next)               # construct TD target
        new_value = current + (self.alpha * (target - current)) # get updated value 
        self.Q[state][action]  = new_value
        self.eps*=self.epsdecay