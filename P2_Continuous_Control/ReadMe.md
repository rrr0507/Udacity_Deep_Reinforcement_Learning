For this project, I am working with the Reacher environment.

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of the agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

Distributed Training
For this project, there is two separate versions of the Unity environment:

The first version contains a single agent.
The second version contains 20 identical agents, each with its own copy of the environment.

I solved the second version with a DDPG agent, which attains average score of 30.04 at 133 episodes.
This folder contains all the results from my project, including a report file in pdf (Project_Report_Continuous_Control.pdf), the saved actor and critic network weights after training (checkpoint_actor.pth, checkpoint_critic.pth), the scores plots (attempt1.png, attempt2.png), the neural network models (model.py), the DDPG agent class (ddpg_multiagent.py), and the jupyter notebook demonstrating the training process (Continuous_Control.ipynb).

The jupyter notebook was run on my own computer with all the dependencies installed and the prebuilt unity Reacher environment downloaded. To run the notebook in the workspace you would need to uncomment the first cell which installs necessary dependencies. Other than that, simply execute the cells step by step and watch the DDPG agent train to solve the environment. 
