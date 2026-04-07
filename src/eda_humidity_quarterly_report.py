import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np


data = pd.read_csv('test.csv')

date = data['date']

mean_hum = data['mean_hum']


date = date.to_numpy()

mean_hum = mean_hum.to_numpy()


myhums = []

mysum1 = []

mycount1 = []

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
           
           
           
           



for i in range(len(mean_hum)):
    if mean_hum[i] == '---':
        mean_hum[i]='-1'


for i in range(40):
    mysum1.append(0)
    mycount1.append(0)
    
 
for i in range(len(mean_hum)):
    
        myyear = str(date[i][0:4])
        
        if(myyear=='2010'):
             
            if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
             
                mysum1[0] = mysum1[0] + float(mean_hum[i])
             
                mycount1[0] = mycount1[0]+1
     
     
            elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
             
               mysum1[1] = mysum1[1] + float(mean_hum[i])
             
               mycount1[1] = mycount1[1]+1
         
            elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
             
               mysum1[2] = mysum1[2] + float(mean_hum[i])
             
               mycount1[2] = mycount1[2]+1
         
         
            else:
             
               mysum1[3] = mysum1[3] + float(mean_hum[i])
             
               mycount1[3] = mycount1[3]+1

        elif(myyear=='2011'):
 
              if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
         
                   mysum1[4] = mysum1[4] + float(mean_hum[i])
         
                   mycount1[4] = mycount1[4]+1
 
 
              elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
         
                   mysum1[5] = mysum1[5] + float(mean_hum[i])
         
                   mycount1[5] = mycount1[5]+1
     
              elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
         
                   mysum1[6] = mysum1[6] + float(mean_hum[i])
         
                   mycount1[6] = mycount1[6]+1
     
     
              else:
         
                   mysum1[7] = mysum1[7] + float(mean_hum[i])
         
                   mycount1[7] = mycount1[7]+1
                   
 
        elif(myyear=='2012'):
               
              if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
               
                   mysum1[8] = mysum1[8] + float(mean_hum[i])
                   
                   mycount1[8] = mycount1[8] + 1
                   
              elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
          
                    mysum1[9] = mysum1[9] + float(mean_hum[i])
          
                    mycount1[9] = mycount1[9]+1
      
              elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
          
                    mysum1[10] = mysum1[10] + float(mean_hum[i])
          
                    mycount1[10] = mycount1[10]+1
      
      
              else:
          
                    mysum1[11] = mysum1[11] + float(mean_hum[i])
          
                    mycount1[11] = mycount1[11]+1  
        elif(myyear=='2013'):
              
             if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
              
                 mysum1[12] = mysum1[12] + float(mean_hum[i])
              
                 mycount1[12] = mycount1[12]+1
      
      
             elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
              
                mysum1[13] = mysum1[13] + float(mean_hum[i])
              
                mycount1[13] = mycount1[13]+1
          
             elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
              
                mysum1[14] = mysum1[14] + float(mean_hum[i])
              
                mycount1[14] = mycount1[14]+1
          
          
             else:
              
                mysum1[15] = mysum1[15] + float(mean_hum[i])
              
                mycount1[15] = mycount1[15]+1

        elif(myyear=='2014'):
  
               if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
          
                    mysum1[16] = mysum1[16] + float(mean_hum[i])
          
                    mycount1[16] = mycount1[16]+1
  
  
               elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
          
                    mysum1[17] = mysum1[17] + float(mean_hum[i])
          
                    mycount1[17] = mycount1[17]+1
      
               elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
          
                    mysum1[18] = mysum1[18] + float(mean_hum[i])
          
                    mycount1[18] = mycount1[18]+1
      
      
               else:
          
                    mysum1[19] = mysum1[19] + float(mean_hum[i])
          
                    mycount1[19] = mycount1[19]+1
                    
  
        elif(myyear=='2015'):
                
               if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                
                    mysum1[20] = mysum1[20] + float(mean_hum[i])
                    
                    mycount1[20] = mycount1[20] + 1
                    
               elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
           
                     mysum1[21] = mysum1[21] + float(mean_hum[i])
           
                     mycount1[21] = mycount1[21]+1
       
               elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
           
                     mysum1[22] = mysum1[22] + float(mean_hum[i])
           
                     mycount1[22] = mycount1[22]+1
       
       
               else:
           
                     mysum1[23] = mysum1[23] + float(mean_hum[i])
           
                     mycount1[23] = mycount1[23]+1 
            
        elif(myyear=='2016'):
                  
              if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                  
                      mysum1[24] = mysum1[24] + float(mean_hum[i])
                      
                      mycount1[24] = mycount1[24] + 1
                      
              elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
             
                       mysum1[25] = mysum1[25] + float(mean_hum[i])
             
                       mycount1[25] = mycount1[25]+1
         
              elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
             
                       mysum1[26] = mysum1[26] + float(mean_hum[i])
             
                       mycount1[26] = mycount1[26]+1
         
         
              else:
             
                       mysum1[27] = mysum1[27] + float(mean_hum[i])
             
                       mycount1[27] = mycount1[27]+1  
                       
        elif(myyear=='2017'):
                 
               if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                 
                    mysum1[28] = mysum1[28] + float(mean_hum[i])
                 
                    mycount1[28] = mycount1[28]+1
         
         
               elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
                 
                   mysum1[29] = mysum1[29] + float(mean_hum[i])
                 
                   mycount1[29] = mycount1[29]+1
             
               elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
                 
                   mysum1[30] = mysum1[30] + float(mean_hum[i])
                 
                   mycount1[30] = mycount1[30]+1
             
             
               else:
                 
                   mysum1[31] = mysum1[31] + float(mean_hum[i])
                 
                   mycount1[31] = mycount1[31]+1

        elif(myyear=='2018'):
     
                  if (date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
             
                       mysum1[32] = mysum1[32] + float(mean_hum[i])
             
                       mycount1[32] = mycount1[32]+1
     
     
                  elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
             
                       mysum1[33] = mysum1[33] + float(mean_hum[i])
             
                       mycount1[33] = mycount1[33]+1
         
                  elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
             
                       mysum1[34] = mysum1[34] + float(mean_hum[i])
             
                       mycount1[34] = mycount1[34]+1
         
         
                  else:
             
                       mysum1[35] = mysum1[35] + float(mean_hum[i])
             
                       mycount1[35] = mycount1[35]+1
                       
     
        elif(myyear=='2019'):
                   
                  if(date[i][5:7]=='01' or date[i][5:7]=='02' or date[i][5:7]=='03'):
                   
                       mysum1[36] = mysum1[36] + float(mean_hum[i])
                       
                       mycount1[36] = mycount1[36] + 1
                       
                  elif (date[i][5:7]=='04' or date[i][5:7]=='05' or date[i][5:7]=='06'):
              
                        mysum1[37] = mysum1[37] + float(mean_hum[i])
              
                        mycount1[37] = mycount1[37]+1
          
                  elif (date[i][5:7]=='07' or date[i][5:7]=='08' or date[i][5:7]=='09'):
              
                        mysum1[38] = mysum1[38] + float(mean_hum[i])
              
                        mycount1[38] = mycount1[38]+1
          
          
                  else:
              
                        mysum1[39] = mysum1[39] + float(mean_hum[i])
              
                        mycount1[39] = mycount1[39]+1   
                        
for i in range(40):
    myhums.append(mysum1[i]/mycount1[i])
    

plt.plot(trimina,myhums,color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Humidity Data")

plt.xticks(rotation = 90)
plt.xlabel('Trimina')
plt.ylabel('Humidity(%)')
plt.title('Humidity Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()

        

                
