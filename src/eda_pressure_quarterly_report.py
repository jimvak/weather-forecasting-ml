import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np



data = pd.read_csv('dataset.csv')

date = data['date']

mean_pres = data['mean_pres']


date = date.to_numpy()

mean_pres = mean_pres.to_numpy()


mypressures = []

mysum2 = []

mycount2 = []

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


for i in range(len(mean_pres)):
    if mean_pres[i] == '---':
        mean_pres[i] = '-1'
        

for i in range(40):
    mysum2.append(0)
    mycount2.append(0)
    
    
for i in range(len(mean_pres)):
      
        myyear = str(date[i][0:4])
      
        if(myyear == '2010'):
            
            if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                mysum2[0] = mysum2[0] + float(mean_pres[i])
                mycount2[0] = mycount2[0] + 1
            
            elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                mysum2[1] = mysum2[1] + float(mean_pres[i])
                mycount2[1] = mycount2[1] + 1
                
            elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                mysum2[2] = mysum2[2] + float(mean_pres[i])
                mycount2[2] = mycount2[2] + 1
             
            else:
                mysum2[3] = mysum2[3] + float(mean_pres[i])
                mycount2[3] = mycount2[3] + 1
         
        elif(myyear == '2011'):
             
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                 mysum2[4] = mysum2[4] + float(mean_pres[i])
                 mycount2[4] = mycount2[4] + 1
             
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                 mysum2[5] = mysum2[5] + float(mean_pres[i])
                 mycount2[5] = mycount2[5] + 1
                 
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                 mysum2[6] = mysum2[6] + float(mean_pres[i])
                 mycount2[6] = mycount2[6] + 1
              
             else:
                 mysum2[7] = mysum2[7] + float(mean_pres[i])
                 mycount2[7] = mycount2[7] + 1   
    
        elif(myyear == '2012'):
              
              if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                  mysum2[8] = mysum2[8] + float(mean_pres[i])
                  mycount2[8] = mycount2[8] + 1
              
              elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                  mysum2[9] = mysum2[9] + float(mean_pres[i])
                  mycount2[9] = mycount2[9] + 1
                  
              elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                  mysum2[10] = mysum2[10] + float(mean_pres[i])
                  mycount2[10] = mycount2[10] + 1
               
              else:
                  mysum2[11] = mysum2[11] + float(mean_pres[i])
                  mycount2[11] = mycount2[11] + 1 
    
        elif(myyear == '2013'):
             
             if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                 mysum2[12] = mysum2[12] + float(mean_pres[i])
                 mycount2[12] = mycount2[12] + 1
             
             elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                 mysum2[13] = mysum2[13] + float(mean_pres[i])
                 mycount2[13] = mycount2[13] + 1
                 
             elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                 mysum2[14] = mysum2[14] + float(mean_pres[i])
                 mycount2[14] = mycount2[14] + 1
              
             else:
                 mysum2[15] = mysum2[15] + float(mean_pres[i])
                 mycount2[15] = mycount2[15] + 1   
    
        elif(myyear == '2014'):
              
              if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                  mysum2[16] = mysum2[16] + float(mean_pres[i])
                  mycount2[16] = mycount2[16] + 1
              
              elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                  mysum2[17] = mysum2[17] + float(mean_pres[i])
                  mycount2[17] = mycount2[17] + 1
                  
              elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                  mysum2[18] = mysum2[18] + float(mean_pres[i])
                  mycount2[18] = mycount2[18] + 1
               
              else:
                  mysum2[19] = mysum2[19] + float(mean_pres[i])
                  mycount2[19] = mycount2[19] + 1 
                  
        elif(myyear == '2015'):
              
              if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                  mysum2[20] = mysum2[20] + float(mean_pres[i])
                  mycount2[20] = mycount2[20] + 1
              
              elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                  mysum2[21] = mysum2[21] + float(mean_pres[i])
                  mycount2[21] = mycount2[21] + 1
                  
              elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                  mysum2[22] = mysum2[22] + float(mean_pres[i])
                  mycount2[22] = mycount2[22] + 1
               
              else:
                  mysum2[23] = mysum2[23] + float(mean_pres[i])
                  mycount2[23] = mycount2[23] + 1   
     
        elif(myyear == '2016'):
               
               if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                   mysum2[24] = mysum2[24] + float(mean_pres[i])
                   mycount2[24] = mycount2[24] + 1
               
               elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                   mysum2[25] = mysum2[25] + float(mean_pres[i])
                   mycount2[25] = mycount2[25] + 1
                   
               elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                   mysum2[26] = mysum2[26] + float(mean_pres[i])
                   mycount2[26] = mycount2[26] + 1
                
               else:
                   mysum2[27] = mysum2[27] + float(mean_pres[i])
                   mycount2[27] = mycount2[27] + 1       
                   
        elif(myyear == '2017'):
              
              if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                  mysum2[28] = mysum2[28] + float(mean_pres[i])
                  mycount2[28] = mycount2[28] + 1
              
              elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                  mysum2[29] = mysum2[29] + float(mean_pres[i])
                  mycount2[29] = mycount2[29] + 1
                  
              elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                  mysum2[30] = mysum2[30] + float(mean_pres[i])
                  mycount2[30] = mycount2[30] + 1
               
              else:
                  mysum2[31] = mysum2[31] + float(mean_pres[i])
                  mycount2[31] = mycount2[31] + 1   
     
        elif(myyear == '2018'):
               
               if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                   mysum2[32] = mysum2[32] + float(mean_pres[i])
                   mycount2[32] = mycount2[32] + 1
               
               elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                   mysum2[33] = mysum2[33] + float(mean_pres[i])
                   mycount2[33] = mycount2[33] + 1
                   
               elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                   mysum2[34] = mysum2[34] + float(mean_pres[i])
                   mycount2[34] = mycount2[34] + 1
                
               else:
                   mysum2[35] = mysum2[35] + float(mean_pres[i])
                   mycount2[35] = mycount2[35] + 1 
           
        else:
                  
               if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                      mysum2[36] = mysum2[36] + float(mean_pres[i])
                      mycount2[36] = mycount2[36] + 1
                  
               elif(date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                      mysum2[37] = mysum2[37] + float(mean_pres[i])
                      mycount2[37] = mycount2[37] + 1
                      
               elif(date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                      mysum2[38] = mysum2[38] + float(mean_pres[i])
                      mycount2[38] = mycount2[38] + 1
                   
               else:
                      mysum2[39] = mysum2[39] + float(mean_pres[i])
                      mycount2[39] = mycount2[39] + 1         
       
        
for i in range(40):
       mypressures.append(mysum2[i]/mycount2[i])
       
       
plt.plot(trimina,mypressures,color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Pressure Data")    
   
plt.xticks(rotation = 90)
plt.xlabel('Trimina')
plt.ylabel('Pressure(hPa)')
plt.title('Pressure Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
