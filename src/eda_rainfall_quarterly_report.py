import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np



data = pd.read_csv('test.csv')

date = data['date']

rain = data['rain']


date = date.to_numpy()

rain = rain.to_numpy()


myrains=[]

mysum3=[]

mycount3=[]

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

for i in range(len(rain)):
    if (rain[i]=='---'):
        rain[i]='-1'

for i in range(40):
    mysum3.append(0)
    mycount3.append(0)
 
for i in range(len(rain)):
    myyear = str(date[i][0:4])
    
    if(myyear=='2010'):
        
          if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
              mysum3[0] = mysum3[0] + float(rain[i])
              mycount3[0] = mycount3[0] + 1
              
          elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
              mysum3[1] = mysum3[1] + float(rain[i])
              mycount3[1] = mycount3[1] + 1
          
          elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
              mysum3[2] = mysum3[2] + float(rain[i])
              mycount3[2] = mycount3[2] + 1
              
          else:
              mysum3[3] = mysum3[3] + float(rain[i])
              mycount3[3] = mycount3[3] + 1
     
    elif(myyear == '2011'):
           
           if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
               mysum3[4] = mysum3[4] + float(rain[i])
               mycount3[4] = mycount3[4] + 1
           
           elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
               mysum3[5] = mysum3[5] + float(rain[i])
               mycount3[5] = mycount3[5] + 1
               
           elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
               mysum3[6] = mysum3[6] + float(rain[i])
               mycount3[6] = mycount3[6] + 1
            
           else:
               mysum3[7] = mysum3[7] + float(rain[i])
               mycount3[7] = mycount3[7] + 1   
  
    elif(myyear == '2012'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum3[8] = mysum3[8] + float(rain[i])
                mycount3[8] = mycount3[8] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum3[9] = mysum3[9] + float(rain[i])
                mycount3[9] = mycount3[9] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum3[10] = mysum3[10] + float(rain[i])
                mycount3[10] = mycount3[10] + 1
             
            else:
                mysum3[11] = mysum3[11] + float(rain[i])
                mycount3[11] = mycount3[11] + 1 
  
    elif(myyear == '2013'):
           
           if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
               mysum3[12] = mysum3[12] + float(rain[i])
               mycount3[12] = mycount3[12] + 1
           
           elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
               mysum3[13] = mysum3[13] + float(rain[i])
               mycount3[13] = mycount3[13] + 1
               
           elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
               mysum3[14] = mysum3[14] + float(rain[i])
               mycount3[14] = mycount3[14] + 1
            
           else:
               mysum3[15] = mysum3[15] + float(rain[i])
               mycount3[15] = mycount3[15] + 1   
  
    elif(myyear == '2014'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum3[16] = mysum3[16] + float(rain[i])
                mycount3[16] = mycount3[16] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum3[17] = mysum3[17] + float(rain[i])
                mycount3[17] = mycount3[17] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum3[18] = mysum3[18] + float(rain[i])
                mycount3[18] = mycount3[18] + 1
             
            else:
                mysum3[19] = mysum3[19] + float(rain[i])
                mycount3[19] = mycount3[19] + 1 
                
    elif(myyear == '2015'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum3[20] = mysum3[20] + float(rain[i])
                mycount3[20] = mycount3[20] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum3[21] = mysum3[21] + float(rain[i])
                mycount3[21] = mycount3[21] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum3[22] = mysum3[22] + float(rain[i])
                mycount3[22] = mycount3[22] + 1
             
            else:
                mysum3[23] = mysum3[23] + float(rain[i])
                mycount3[23] = mycount3[23] + 1   
   
    elif(myyear == '2016'):
             
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                 mysum3[24] = mysum3[24] + float(rain[i])
                 mycount3[24] = mycount3[24] + 1
             
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                 mysum3[25] = mysum3[25] + float(rain[i])
                 mycount3[25] = mycount3[25] + 1
                 
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                 mysum3[26] = mysum3[26] + float(rain[i])
                 mycount3[26] = mycount3[26] + 1
              
             else:
                 mysum3[27] = mysum3[27] + float(rain[i])
                 mycount3[27] = mycount3[27] + 1       
                 
    elif(myyear == '2017'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum3[28] = mysum3[28] + float(rain[i])
                mycount3[28] = mycount3[28] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum3[29] = mysum3[29] + float(rain[i])
                mycount3[29] = mycount3[29] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum3[30] = mysum3[30] + float(rain[i])
                mycount3[30] = mycount3[30] + 1
             
            else:
                mysum3[31] = mysum3[31] + float(rain[i])
                mycount3[31] = mycount3[31] + 1   
   
    elif(myyear == '2018'):
             
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                 mysum3[32] = mysum3[32] + float(rain[i])
                 mycount3[32] = mycount3[32] + 1
             
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                 mysum3[33] = mysum3[33] + float(rain[i])
                 mycount3[33] = mycount3[33] + 1
                 
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                 mysum3[34] = mysum3[34] + float(rain[i])
                 mycount3[34] = mycount3[34] + 1
              
             else:
                 mysum3[35] = mysum3[35] + float(rain[i])
                 mycount3[35] = mycount3[35] + 1 
         
    else:
                
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                    mysum3[36] = mysum3[36] + float(rain[i])
                    mycount3[36] = mycount3[36] + 1
                
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                    mysum3[37] = mysum3[37] + float(rain[i])
                    mycount3[37] = mycount3[37] + 1
                    
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                    mysum3[38] = mysum3[38] + float(rain[i])
                    mycount3[38] = mycount3[38] + 1
                 
             else:
                    mysum3[39] = mysum3[39] + float(rain[i])
                    mycount3[39] = mycount3[39] + 1                  
                    
        
for i in range(40):
       myrains.append(mysum3[i]/mycount3[i])       

plt.plot(trimina,myrains,color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Rainfall Data")    
   
plt.xticks(rotation = 90)
plt.xlabel('Trimina')
plt.ylabel('Rainfall(mm)')
plt.title('Rainfall Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()            
