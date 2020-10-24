from argparse import ArgumentParser
from tqdm import tqdm
import numpy as np
import os
import random
import gym3
from procgen import ProcgenGym3Env
import time
from matplotlib import pyplot as plt
import copy

from modules import *
from utils import *

"""
########################################
TO DO:

	- make sure ppo solo works
	- how to train routing network? (distance clustering?)

	1. train cluster algorithm on latent space
	2. train agent using clustered feature modularizer

########################################
"""

if __name__ == '__main__':

	parser = ArgumentParser(add_help=False)

	# experiment and  environment
	parser.add_argument('--experiment_name', default="LunarLander-Modularized", type=str)
	parser.add_argument('--env_names', default=["LunarLander-v2",])

	# saving options
	parser.add_argument('--log', default=True, type=bool)
	parser.add_argument('--graph', default=True, type=bool)

	# training params
	parser.add_argument('--random_seeds', default=list(range(1)), type=list)
	parser.add_argument('--n_steps', default=12000, type=int)
	parser.add_argument('--batch_sz', default=64, type=int)
	parser.add_argument('--gamma', default=0.99, type=float)
	parser.add_argument('--k_epochs', default=4, type=int)
	parser.add_argument('--n_envs', default=4, type=int)
	parser.add_argument('--update_step', default=1200, type=int)

	# model params
	parser.add_argument('--actor_lr', default=5e-4, type=float)
	parser.add_argument('--critic_lr', default=5e-4, type=float)
	parser.add_argument('--epsilon', default=0.2, type=float)

	params = parser.parse_args()

	run_experiment(PPO, params)
