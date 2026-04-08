import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np


data = pd.read_csv('data/dataset.csv')

date = data['date']

dir_wind = data['dir_wind']


date = date.to_numpy()


dir_wind = dir_wind.to_numpy()

mysum5=[]

mycount5=[]

mywinds=[]

#directions=np.unique(dir_wind)

#new_array=[-1.0,90,67.5,112.5,0,45,22.5,337.5,315,180,135,157.5,202.5,225,270,292.5,247.5]

trimina = ['1o - 10','2o - 10', '3o - 10', '4o - 10',
           
           '1o - 11','2o - 11', '3o - 11', '4o - 11',
           
           '1o - 12','2o - 12', '3o - 12', '4o - 12',
           
           '1o - 13','2o - 13', '3o - 13', '4o - 13',
           
           '1o - 14','2o - 14', '3o - 14', '4o - 14',
           
           '1o - 15','2o - 15', '3o - 15', '4o - 15',
           
           '1o - 16','2o - 16', '3o - 16', '4o - 16',
           
           '1o - 17','2o - 17', '3o - 17', '4o - 17',
           
           '1o - 18','2o - 18', '3o - 18', '4o - 18',
           
           '1o - 19','2o - 19', '3o - 19', '4o - 19']


for i in range(len(dir_wind)):
    
    if(dir_wind[i]=='---'):
        dir_wind[i]=float('-1')
       
    elif(dir_wind[i]=='E'):
        dir_wind[i]=float('90')
        
    elif(dir_wind[i]=='ENE'):
        dir_wind[i]=float('67.5')
   
    elif(dir_wind[i]=='ESE'):
        dir_wind[i]=float('112.5')
#        
    elif(dir_wind[i]=='N'):
        dir_wind[i]=float('0')
#    
    elif(dir_wind[i]=='NE'):
        dir_wind[i]=float('45')
#        
    elif(dir_wind[i]=='NNE'):
        dir_wind[i]=float('22.5')
#    
    elif(dir_wind[i]=='NNW'):
        dir_wind[i]=float('337.5')
#        
    elif(dir_wind[i]=='NW'):
        dir_wind[i]=float('315')
#    
    elif(dir_wind[i]=='S'):
        dir_wind[i]=float('180')
#        
    elif(dir_wind[i]=='SE'):
        dir_wind[i]=float('135')
#        
    elif(dir_wind[i]=='SSE'):
        dir_wind[i]=float('157.5')
#        
    elif(dir_wind[i]=='SSW'):
        dir_wind[i]=float('202.5')
#    
    elif(dir_wind[i]=='SW'):
        dir_wind[i]=float('225')
#        
    elif(dir_wind[i]=='W'):
        dir_wind[i]=float('270')
#    
    elif(dir_wind[i]=='WNW'):
       dir_wind[i]=float('292.5')
#       
    elif(dir_wind[i]=='WSW'):
        dir_wind[i]=float('247.5')
        
        
final_wind_dir = []


for x in dir_wind:
    final_wind_dir.append(float(x))
    


k = 0

etos = 2010

for i in range(10):
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(final_wind_dir[k:90+k])
    axs[0, 0].set_title('Proto Trimino '+str(etos))
    axs[0, 1].plot(final_wind_dir[91+k:182+k], 'tab:orange')
    axs[0, 1].set_title('Deytero Trimino ' + str(etos))
    axs[1, 0].plot(final_wind_dir[183+k:273+k], 'tab:green')
    axs[1, 0].set_title('Trito Trimino ' + str(etos))
    axs[1, 1].plot(final_wind_dir[274+k:365+k], 'tab:red')
    axs[1, 1].set_title('Tetarto Trimino ' + str(etos))
    
    for ax in axs.flat:
        ax.set(xlabel='Day', ylabel='Wind Direction')
    
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
    k=k+365
    etos=etos+1










    
        
 
