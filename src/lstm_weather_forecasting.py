import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from sklearn import preprocessing

from sklearn.model_selection import train_test_split




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
    
    temp_list.append(final_mean_speed[i])
    temp_list.append(final_rain[i])
    temp_list.append(final_mean_pres[i])
    temp_list.append(final_dir_wind[i]) 
    temp_list.append(final_mean_temp[i])
    
    temp_list.append(final_mean_hum[i])
    final_data.append(temp_list)
    
final_data = np.array(final_data)



#input data
X =  final_data[:,:5]

#output data
y = final_data[:,5]


#kanoume expand to dimension kai sto X kai sto y
#etsi oste na mporei na einai apodeikti i eisodos sto LSTM


X = np.expand_dims(X, axis=2)

y = np.expand_dims(y, axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

import tensorflow as tf



batch_size = 1

model=Sequential()
model.add(LSTM(64, batch_input_shape=(batch_size,5,1), stateful=True))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')


history = model.fit(X_train,y_train, epochs=10, batch_size=batch_size, verbose=2, shuffle=True)



provlepseis= model.predict(X_test)

#plt.title('humidity loss')
#plt.plot(history.history['loss'], label='epochs')
#plt.legend()
#plt.show()
