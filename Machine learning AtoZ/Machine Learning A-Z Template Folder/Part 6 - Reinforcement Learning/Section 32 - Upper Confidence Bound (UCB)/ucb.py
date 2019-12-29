# Upper Confidence Bound

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
N = 10000
d = 10
total_reward = 0
numbers_of_selections = [0] * d
sum_of_rewards = [0] * d
ads_selected = []
for n in range(0,N):
    max_uper_bound = 0
    ad = 0
    for i in range (0,d):
        if (numbers_of_selections[i] > 0):
          average_reward = sum_of_rewards[i]/numbers_of_selections[i]
          delta_i=  math.sqrt(3/2*math.log(n+1))/numbers_of_selections[i]
          upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_uper_bound:
          max_uper_bound = upper_bound
          ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] + 1
    reward = dataset.values[n,ad]
    sum_of_rewards[ad] += reward
    total_reward += reward
    