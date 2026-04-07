import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np


data = pd.read_csv('test.csv')

date = data['date']

mean_temp = data['mean_temp']


date = date.to_numpy()

mean_temp = mean_temp.to_numpy()

        
    
mytemps = []

mysum = []

mycount = []


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
           
           
           
           

for i in range(len(mean_temp)):
    if mean_temp[i]=='---':
        mean_temp[i]='-1'


for i in range(40):
    mysum.append(0)
    mycount.append(0)

for i in range(len(mean_temp)):
    
    myyear = str(date[i][0:4])
    
    if(myyear=='2010'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[0] = mysum[0] + float(mean_temp[i])
            
            mycount[0] = mycount[0]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[1] = mysum[1] + float(mean_temp[i])
            
            mycount[1] = mycount[1]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[2] = mysum[2] + float(mean_temp[i])
            
            mycount[2] = mycount[2]+1
        
        
        else:
            
            mysum[3] = mysum[3] + float(mean_temp[i])
            
            mycount[3] = mycount[3]+1
            
    elif(myyear=='2011'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[4] = mysum[4] + float(mean_temp[i])
            
            mycount[4] = mycount[4]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[5] = mysum[5] + float(mean_temp[i])
            
            mycount[5] = mycount[5]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[6] = mysum[6] + float(mean_temp[i])
            
            mycount[6] = mycount[6]+1
        
        
        else:
            
            mysum[7] = mysum[7] + float(mean_temp[i])
            
            mycount[7] = mycount[7]+1
    
    elif(myyear=='2012'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[8] = mysum[8] + float(mean_temp[i])
            
            mycount[8] = mycount[8]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[9] = mysum[9] + float(mean_temp[i])
            
            mycount[9] = mycount[9]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[10] = mysum[10] + float(mean_temp[i])
            
            mycount[10] = mycount[10]+1
        
        
        else:
            
            mysum[11] = mysum[11] + float(mean_temp[i])
            
            mycount[11] = mycount[11]+1 
            
    elif(myyear=='2013'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[12] = mysum[12] + float(mean_temp[i])
            
            mycount[12] = mycount[12]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[13] = mysum[13] + float(mean_temp[i])
            
            mycount[13] = mycount[13]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[14] = mysum[14] + float(mean_temp[i])
            
            mycount[14] = mycount[14]+1
        
        
        else:
            
            mysum[15] = mysum[15] + float(mean_temp[i])
            
            mycount[15] = mycount[15]+1  
    
    elif(myyear=='2014'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[16] = mysum[16] + float(mean_temp[i])
            
            mycount[16] = mycount[16]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[17] = mysum[17] + float(mean_temp[i])
            
            mycount[17] = mycount[17]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[18] = mysum[18] + float(mean_temp[i])
            
            mycount[18] = mycount[18]+1
        
        
        else:
            
            mysum[19] = mysum[19] + float(mean_temp[i])
            
            mycount[19] = mycount[19]+1
    
    
    elif(myyear=='2015'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[20] = mysum[20] + float(mean_temp[i])
            
            mycount[20] = mycount[20]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[21] = mysum[21] + float(mean_temp[i])
            
            mycount[21] = mycount[21]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[22] = mysum[22] + float(mean_temp[i])
            
            mycount[22] = mycount[22]+1
        
        
        else:
            
            mysum[23] = mysum[23] + float(mean_temp[i])
            
            mycount[23] = mycount[23]+1
    
    elif(myyear=='2016'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[24] = mysum[24] + float(mean_temp[i])
            
            mycount[24] = mycount[24]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[25] = mysum[25] + float(mean_temp[i])
            
            mycount[25] = mycount[25]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[26] = mysum[26] + float(mean_temp[i])
            
            mycount[26] = mycount[26]+1
        
        
        else:
            
            mysum[27] = mysum[27] + float(mean_temp[i])
            
            mycount[27] = mycount[27]+1
            
    elif(myyear=='2017'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[28] = mysum[28] + float(mean_temp[i])
            
            mycount[28] = mycount[28]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[29] = mysum[29] + float(mean_temp[i])
            
            mycount[29] = mycount[29]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[30] = mysum[30] + float(mean_temp[i])
            
            mycount[30] = mycount[30]+1
        
        
        else:
            
            mysum[31] = mysum[31] + float(mean_temp[i])
            
            mycount[31] = mycount[31]+1
    
        
    elif(myyear=='2018'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[32] = mysum[32] + float(mean_temp[i])
            
            mycount[32] = mycount[32]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[33] = mysum[33] + float(mean_temp[i])
            
            mycount[33] = mycount[33]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[34] = mysum[34] + float(mean_temp[i])
            
            mycount[34] = mycount[34]+1
        
        
        else:
            
            mysum[35] = mysum[35] + float(mean_temp[i])
            
            mycount[35] = mycount[35]+1
    
    
    
    elif(myyear=='2019'):
    
        if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
            
            mysum[36] = mysum[36] + float(mean_temp[i])
            
            mycount[36] = mycount[36]+1
    
    
        elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
            
            mysum[37] = mysum[37] + float(mean_temp[i])
            
            mycount[37] = mycount[37]+1
        
        elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
            
            mysum[38] = mysum[38] + float(mean_temp[i])
            
            mycount[38] = mycount[38]+1
        
        
        else:
            
            mysum[39] = mysum[39] + float(mean_temp[i])
            
            mycount[39] = mycount[39]+1
            
            
for i in range(40):
    mytemps.append(mysum[i]/mycount[i])
    
    
    
plt.plot(trimina, mytemps, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Temperature Data")
  
plt.xticks(rotation = 90)
plt.xlabel('Trimina')
plt.ylabel('Temperature(°C)')
plt.title('Temperature Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()



   
