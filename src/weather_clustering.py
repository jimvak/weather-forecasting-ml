import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from sklearn import preprocessing

from sklearn.model_selection import train_test_split

from sklearn.cluster import KMeans

from sklearn.cluster import DBSCAN

from sklearn.cluster import AgglomerativeClustering

from sklearn import metrics

from sklearn.cluster import SpectralClustering

from sklearn.cluster import OPTICS

data = pd.read_csv('dataset.csv')

temp = data['mean_temp']


mean_temp = temp.to_numpy()

sum_temp = 0.0

count_temp=0

final_mean_temp=[]

for x in mean_temp:
    if x!='---':
        sum_temp=sum_temp+float(x)
        count_temp=count_temp + 1
        
avg_temp=sum_temp/count_temp


for x in mean_temp:
    if x == '---':
        final_mean_temp.append(avg_temp)
    else:
        final_mean_temp.append(float(x))
    



        
hum = data['mean_hum']

mean_hum = hum.to_numpy()

sum_hum = 0.0

count_hum=0

final_mean_hum=[]

for x in mean_hum:
    if x!='---':
        sum_hum=sum_hum+float(x)
        count_hum=count_hum + 1
        
avg_hum=sum_hum/count_hum


for x in mean_hum:
    if x == '---':
        final_mean_hum.append(avg_hum)
    else:
        final_mean_hum.append(float(x))
    



pres = data['mean_pres']

mean_pres = pres.to_numpy()

sum_pres = 0.0

count_pres=0

final_mean_pres=[]

for x in mean_pres:
    if x!='---':
        sum_pres=sum_pres+float(x)
        count_pres=count_pres + 1
        
avg_pres=sum_pres/count_pres


for x in mean_pres:
    if x == '---':
        final_mean_pres.append(avg_pres)
    else:
        final_mean_pres.append(float(x))     





rain = data['rain']

rain = rain.to_numpy()

sum_rain = 0.0

count_rain=0

final_rain=[]

for x in rain:
    if x!='---':
        sum_rain=sum_rain+float(x)
        count_rain=count_rain + 1
        
avg_rain=sum_rain/count_rain


for x in rain:
    if x == '---':
        final_rain.append(avg_rain)
    else:
        final_rain.append(float(x)) 
        
        

mean_speed = data['mean_speed_wind']

mean_speed = mean_speed.to_numpy()

sum_speed = 0.0

count_speed=0

final_mean_speed=[]

for x in mean_speed:
    if x!='---':
        sum_speed=sum_speed+float(x)
        count_speed=count_speed + 1
        
avg_speed=sum_speed/count_speed


for x in mean_speed:
    if x == '---':
        final_mean_speed.append(avg_speed)
    else:
        final_mean_speed.append(float(x))        




dir_wind = data['dir_wind']

dir_wind = dir_wind.to_numpy()

sum_dir_wind = 0.0

count_dir_wind=0




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
        

final_dir_wind=[]    

for x in dir_wind:
     if x!='---':
         sum_dir_wind=sum_dir_wind+float(x)
         count_dir_wind=count_dir_wind + 1
         
avg_dir_wind=sum_dir_wind/count_dir_wind


for x in dir_wind:
     if x == '---':
         final_dir_wind.append(avg_speed)
     else:
         final_dir_wind.append(float(x))
         
         
#enopoihsh twn dedomenwn 


final_data = []

for i in range(len(final_rain)):
    temp_list = []
    temp_list.append(final_dir_wind[i])
    temp_list.append(final_mean_hum[i])
    temp_list.append(final_mean_pres[i])
    temp_list.append(final_mean_speed[i])
    temp_list.append(final_mean_temp[i])
    temp_list.append(final_rain[i])
    final_data.append(temp_list)
    
final_data = np.array(final_data)

X=final_data

#efarmozw kmeans algorithmo

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

etiketes1=kmeans.labels_

#efarmozw DBSCAN algorithmo den mas kanei giati oi etiketes exoun arnitikes times

#dbscan = DBSCAN(eps=0.2, min_samples=2).fit(X)

#etiketes2=dbscan.labels_

#efarmozw agglomerative algorithmo

agglomer = AgglomerativeClustering().fit(X)

etiketes3=agglomer.labels_

#efarmozw spectral clustering

#spectClust = SpectralClustering(n_clusters=2,assign_labels='discretize',random_state=0).fit(X)

#etiketes4=spectClust.labels_

#efarmozw OPTICS de mas kanei

#optics = OPTICS(min_samples=2).fit(X) 

#etiketes5=optics.labels_

#ypologizw tin metriki silhouette

#print(metrics.silhouette_score(X,etiketes1,metric='euclidean'))

#print(metrics.silhouette_score(X,etiketes3,metric='euclidean'))


#simplironw tis thermokrasies xrisimopoiontas tis times tou kmeans
sum_temper1=0.0
count_temper1=0


for i in range(len(final_data)):
   if etiketes1[i]==0:
             sum_temper1=sum_temper1+float(final_data[i][4])
             count_temper1=count_temper1+1
             
average_temper1=sum_temper1/count_temper1

 
sum_temper2=0.0
count_temper2=0       
 
for i in range(len(final_data)):
   if etiketes1[i]==1:
             sum_temper2=sum_temper2+float(final_data[i][4])
             count_temper2=count_temper2+1
             
average_temper2=sum_temper2/count_temper2


             
#simplironw tis thermokrasies xrisimopoiontas tis times tou Agglomerative

sum_temper3=0.0

count_temper3=0


for i in range(len(final_data)):
   if etiketes3[i]==0:
             sum_temper3=sum_temper3+float(final_data[i][4])
             count_temper3=count_temper3+1
             
average_temper3=sum_temper3/count_temper3


sum_temper4=0.0

count_temper4=0

for i in range(len(final_data)):
   if etiketes3[i]==1:
             sum_temper4=sum_temper4+float(final_data[i][4])
             count_temper4=count_temper4+1
             
average_temper4=sum_temper4/count_temper4


#simplironw ta humidities xrisimopoiontas tis times tou kmeans

sum_humidity1=0.0
count_humidity1=0


for i in range(len(final_data)):
    if etiketes1[i]==0:
        sum_humidity1=sum_humidity1+float(final_data[i][1])
        count_humidity1=count_humidity1+1

average_humidity1=sum_humidity1/count_humidity1

 
sum_humidity2=0.0
count_humidity2=0


for i in range(len(final_data)):
    if etiketes1[i]==1:
        sum_humidity2=sum_humidity2+float(final_data[i][1])
        count_humidity2=count_humidity2+1

average_humidity2=sum_humidity2/count_humidity2


         
#simplironw ta humidities xrisimopoiontas tis times tou Agglomerative

sum_humidity3=0.0

count_humidity3=0


for i in range(len(final_data)):
   if etiketes3[i]==0:
             sum_humidity3=sum_humidity3+float(final_data[i][1])
             count_humidity3=count_humidity3+1
             
average_humidity3=sum_humidity3/count_humidity3


sum_humidity4=0.0

count_humidity4=0

for i in range(len(final_data)):
   if etiketes3[i]==1:
             sum_humidity4=sum_humidity4+float(final_data[i][1])
             count_humidity4=count_humidity4+1
             
average_humidity4=sum_humidity4/count_humidity4

#simplironw ta pressures xrisimopoiontas tis times tou kmeans
sum_pres1=0.0
count_pres1=0


for i in range(len(final_data)):
   if etiketes1[i]==0:
             sum_pres1=sum_pres1+float(final_data[i][2])
             count_pres1=count_pres1+1
             
average_pres1=sum_pres1/count_pres1

 
sum_pres2=0.0
count_pres2=0       
 
for i in range(len(final_data)):
   if etiketes1[i]==1:
             sum_pres2=sum_pres2+float(final_data[i][2])
             count_pres2=count_pres2+1
             
average_pres2=sum_pres2/count_pres2


             
#simplironw ta pressures xrisimopoiontas tis times tou Agglomerative

sum_pres3=0.0

count_pres3=0


for i in range(len(final_data)):
   if etiketes3[i]==0:
             sum_pres3=sum_pres3+float(final_data[i][2])
             count_pres3=count_pres3+1
             
average_pres3=sum_pres3/count_pres3


sum_pres4=0.0

count_pres4=0

for i in range(len(final_data)):
   if etiketes3[i]==1:
             sum_pres4=sum_pres4+float(final_data[i][2])
             count_pres4=count_pres4+1
             
average_pres4=sum_pres4/count_pres4


#simplironw ta speed wind xrisimopoiontas tis times tou kmeans
sum_speed1=0.0
count_speed1=0


for i in range(len(final_data)):
   if etiketes1[i]==0:
             sum_speed1=sum_speed1+float(final_data[i][3])
             count_speed1=count_speed1+1
             
average_speed1=sum_speed1/count_speed1

 
sum_speed2=0.0
count_speed2=0       
 
for i in range(len(final_data)):
   if etiketes1[i]==1:
             sum_speed2=sum_speed2+float(final_data[i][3])
             count_speed2=count_speed2+1
             
average_speed2=sum_speed2/count_speed2


             
#simplironw ta speed wind xrisimopoiontas tis times tou Agglomerative

sum_speed3=0.0

count_speed3=0


for i in range(len(final_data)):
   if etiketes3[i]==0:
             sum_speed3=sum_speed3+float(final_data[i][3])
             count_speed3=count_speed3+1
             
average_speed3=sum_speed3/count_speed3


sum_speed4=0.0

count_speed4=0

for i in range(len(final_data)):
   if etiketes3[i]==1:
             sum_speed4=sum_speed4+float(final_data[i][3])
             count_speed4=count_speed4+1
             
average_speed4=sum_speed4/count_speed4
        

#simplironw ta rains xrisimopoiontas tis times tou kmeans
sum_rain1=0.0
count_rain1=0


for i in range(len(final_data)):
   if etiketes1[i]==0:
             sum_rain1=sum_rain1+float(final_data[i][5])
             count_rain1=count_rain1+1
             
average_rain1=sum_rain1/count_rain1

 
sum_rain2=0.0
count_rain2=0       
 
for i in range(len(final_data)):
   if etiketes1[i]==1:
             sum_rain2=sum_rain2+float(final_data[i][5])
             count_rain2=count_rain2+1
             
average_rain2=sum_rain2/count_rain2


             
#simplironw rains xrisimopoiontas tis times tou Agglomerative

sum_rain3=0.0

count_rain3=0


for i in range(len(final_data)):
   if etiketes3[i]==0:
             sum_rain3=sum_rain3+float(final_data[i][5])
             count_rain3=count_rain3+1
             
average_rain3=sum_rain3/count_rain3


sum_rain4=0.0

count_rain4=0

for i in range(len(final_data)):
   if etiketes3[i]==1:
             sum_rain4=sum_rain4+float(final_data[i][5])
             count_rain4=count_rain4+1
             
average_rain4=sum_rain4/count_rain4
