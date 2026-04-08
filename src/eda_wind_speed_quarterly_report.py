import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np



data = pd.read_csv('data/dataset.csv')

date = data['date']

mean_speed_wind = data['mean_speed_wind']


date = date.to_numpy()

mean_speed_wind = mean_speed_wind.to_numpy()


myspeeds = []

mysum4 = []

mycount4 = []



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

for i in range(len(mean_speed_wind)):
    if(mean_speed_wind[i]=='---'):
        mean_speed_wind[i]='-1'
           
for i in range(40):
    mysum4.append(0)
    mycount4.append(0)
    
for i in range(len(mean_speed_wind)):
    myyear = str(date[i][0:4])
    
    if(myyear=='2010'):
        
          if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
              mysum4[0] = mysum4[0] + float(mean_speed_wind[i])
              mycount4[0] = mycount4[0] + 1
              
          elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
              mysum4[1] = mysum4[1] + float(mean_speed_wind[i])
              mycount4[1] = mycount4[1] + 1
          
          elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
              mysum4[2] = mysum4[2] + float(mean_speed_wind[i])
              mycount4[2] = mycount4[2] + 1
              
          else:
              mysum4[3] = mysum4[3] + float(mean_speed_wind[i])
              mycount4[3] = mycount4[3] + 1
     
    elif(myyear == '2011'):
           
           if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
               mysum4[4] = mysum4[4] + float(mean_speed_wind[i])
               mycount4[4] = mycount4[4] + 1
           
           elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
               mysum4[5] = mysum4[5] + float(mean_speed_wind[i])
               mycount4[5] = mycount4[5] + 1
               
           elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
               mysum4[6] = mysum4[6] + float(mean_speed_wind[i])
               mycount4[6] = mycount4[6] + 1
            
           else:
               mysum4[7] = mysum4[7] + float(mean_speed_wind[i])
               mycount4[7] = mycount4[7] + 1   
  
    elif(myyear == '2012'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum4[8] = mysum4[8] + float(mean_speed_wind[i])
                mycount4[8] = mycount4[8] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum4[9] = mysum4[9] + float(mean_speed_wind[i])
                mycount4[9] = mycount4[9] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum4[10] = mysum4[10] + float(mean_speed_wind[i])
                mycount4[10] = mycount4[10] + 1
             
            else:
                mysum4[11] = mysum4[11] + float(mean_speed_wind[i])
                mycount4[11] = mycount4[11] + 1 
  
    elif(myyear == '2013'):
           
           if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
               mysum4[12] = mysum4[12] + float(mean_speed_wind[i])
               mycount4[12] = mycount4[12] + 1
           
           elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
               mysum4[13] = mysum4[13] + float(mean_speed_wind[i])
               mycount4[13] = mycount4[13] + 1
               
           elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
               mysum4[14] = mysum4[14] + float(mean_speed_wind[i])
               mycount4[14] = mycount4[14] + 1
            
           else:
               mysum4[15] = mysum4[15] + float(mean_speed_wind[i])
               mycount4[15] = mycount4[15] + 1   
  
    elif(myyear == '2014'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum4[16] = mysum4[16] + float(mean_speed_wind[i])
                mycount4[16] = mycount4[16] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum4[17] = mysum4[17] + float(mean_speed_wind[i])
                mycount4[17] = mycount4[17] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum4[18] = mysum4[18] + float(mean_speed_wind[i])
                mycount4[18] = mycount4[18] + 1
             
            else:
                mysum4[19] = mysum4[19] + float(mean_speed_wind[i])
                mycount4[19] = mycount4[19] + 1 
                
    elif(myyear == '2015'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum4[20] = mysum4[20] + float(mean_speed_wind[i])
                mycount4[20] = mycount4[20] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum4[21] = mysum4[21] + float(mean_speed_wind[i])
                mycount4[21] = mycount4[21] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum4[22] = mysum4[22] + float(mean_speed_wind[i])
                mycount4[22] = mycount4[22] + 1
             
            else:
                mysum4[23] = mysum4[23] + float(mean_speed_wind[i])
                mycount4[23] = mycount4[23] + 1   
   
    elif(myyear == '2016'):
             
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                 mysum4[24] = mysum4[24] + float(mean_speed_wind[i])
                 mycount4[24] = mycount4[24] + 1
             
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                 mysum4[25] = mysum4[25] + float(mean_speed_wind[i])
                 mycount4[25] = mycount4[25] + 1
                 
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                 mysum4[26] = mysum4[26] + float(mean_speed_wind[i])
                 mycount4[26] = mycount4[26] + 1
              
             else:
                 mysum4[27] = mysum4[27] + float(mean_speed_wind[i])
                 mycount4[27] = mycount4[27] + 1       
                 
    elif(myyear == '2017'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum4[28] = mysum4[28] + float(mean_speed_wind[i])
                mycount4[28] = mycount4[28] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum4[29] = mysum4[29] + float(mean_speed_wind[i])
                mycount4[29] = mycount4[29] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum4[30] = mysum4[30] + float(mean_speed_wind[i])
                mycount4[30] = mycount4[30] + 1
             
            else:
                mysum4[31] = mysum4[31] + float(mean_speed_wind[i])
                mycount4[31] = mycount4[31] + 1   
   
    elif(myyear == '2018'):
             
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                 mysum4[32] = mysum4[32] + float(mean_speed_wind[i])
                 mycount4[32] = mycount4[32] + 1
             
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                 mysum4[33] = mysum4[33] + float(mean_speed_wind[i])
                 mycount4[33] = mycount4[33] + 1
                 
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                 mysum4[34] = mysum4[34] + float(mean_speed_wind[i])
                 mycount4[34] = mycount4[34] + 1
              
             else:
                 mysum4[35] = mysum4[35] + float(mean_speed_wind[i])
                 mycount4[35] = mycount4[35] + 1 
         
    else:
                
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                    mysum4[36] = mysum4[36] + float(mean_speed_wind[i])
                    mycount4[36] = mycount4[36] + 1
                
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                    mysum4[37] = mysum4[37] + float(mean_speed_wind[i])
                    mycount4[37] = mycount4[37] + 1
                    
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                    mysum4[38] = mysum4[38] + float(mean_speed_wind[i])
                    mycount4[38] = mycount4[38] + 1
                 
             else:
                    mysum4[39] = mysum4[39] + float(mean_speed_wind[i])
                    mycount4[39] = mycount4[39] + 1                  
                    
        
for i in range(40):
       myspeeds.append(mysum4[i]/mycount4[i])       

plt.plot(trimina,myspeeds,color = 'g', linestyle = 'dashed',
         marker = 'o',label = "WInd Speed Data")    
   
plt.xticks(rotation = 90)
plt.xlabel('Trimina')
plt.ylabel('Wind Speed')
plt.title('Wind Speed Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()       
