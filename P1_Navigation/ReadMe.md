This folder contains the project submission for P1 Navigation. For this project, we need to train an agent to navigate in a large, square world.

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

0 - move forward.
1 - move backward.
2 - turn left.
3 - turn right.

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

The main codes are all in the jupyter notebook Navigation.ipynb including the necessary classes and helper functions. 
The pdf file contains the project report and results.
The model.pth file contains saved model weights.
Run all cells in the jupyter notebook to see the training results of the Double-DQN agent.
The code was written in the Udacity workspace. and the necessary packages and environments are loaded by the first few cells of the notebook in the Udacity workspace, which already has certain packages installed and the environment saved.
