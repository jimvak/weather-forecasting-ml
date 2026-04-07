import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np


data = pd.read_csv('test.csv')

wind = data['mean_speed_wind']


mean_wind = wind.to_numpy()

final_mean_wind = []

for x in mean_wind:
    if x=='---':
        final_mean_wind.append(-1)
    else:
        final_mean_wind.append(float(x))


    


k = 0

etos = 2010

for i in range(10):
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(final_mean_wind[k:90+k])
    axs[0, 0].set_title('Proto Trimino '+str(etos))
    axs[0, 1].plot(final_mean_wind[91+k:182+k], 'tab:orange')
    axs[0, 1].set_title('Deytero Trimino ' + str(etos))
    axs[1, 0].plot(final_mean_wind[183+k:273+k], 'tab:green')
    axs[1, 0].set_title('Trito Trimino ' + str(etos))
    axs[1, 1].plot(final_mean_wind[274+k:365+k], 'tab:red')
    axs[1, 1].set_title('Tetarto Trimino ' + str(etos))
    
    for ax in axs.flat:
        ax.set(xlabel='Day', ylabel='Mean WInd Speed')
    
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
    k=k+365
    etos=etos+1
