import csv

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from sklearn import preprocessing

from sklearn.model_selection import train_test_split

from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier

from sklearn.datasets import make_classification

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from sklearn import preprocessing
from sklearn import utils
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from sklearn.naive_bayes import GaussianNB

data = pd.read_csv('test.csv')

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
    temp_list.append(final_rain[i])
    temp_list.append(final_mean_temp[i])
    temp_list.append(final_mean_speed[i])
    temp_list.append(final_mean_pres[i])
    temp_list.append(final_dir_wind[i])
    temp_list.append(final_mean_hum[i])
    final_data.append(temp_list)
    
final_data = np.array(final_data)

#efarmozoume random forest 

#input data
X = final_data[:,:5]

#output data
y = final_data[:,5]

lab_enc = preprocessing.LabelEncoder()

y = lab_enc.fit_transform ( y ) 

#diaspasi se train set kai test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#dimiourgoume to montelo toy RandomForestClassifier 
clf = RandomForestClassifier(max_depth=2, random_state=0)

#ekpaideysi 
clf.fit(X_train, y_train)

#provlepsi 
y_pred=clf.predict(X_test)

#ypologizoume to precision
#precision = precision_score(y_test, y_pred, average = 'micro')

#print('Precision: %.3f' % precision)








#efarmozoume knn

#input data
X1 = final_data[:,:5]

#output data
y1 = final_data[:,5]

lab_enc = preprocessing.LabelEncoder()

y1 = lab_enc.fit_transform ( y1 ) 

#diaspasi se train set kai test set 
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.20)

#dimiourgoume to montelo tou knn
neigh = KNeighborsClassifier(n_neighbors=5)

#ekpaideysi
neigh.fit(X1_train, y1_train)

#provlepsi
y1_pred=neigh.predict(X1_test)

#ypologizoume to precision
#precision = precision_score(y1_test, y1_pred, average = 'micro')

#print('Precision: %.3f' % precision)









#efarmozoume logistic regression

#input data
X2 = final_data[:,:5]

#output data
y2 = final_data[:,5]

lab_enc = preprocessing.LabelEncoder()

y2 = lab_enc.fit_transform ( y2 ) 


#diaspasi se train set kai test set 
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.20)

#dimiourgoume to montelo tou logistic regression
clf2 = LogisticRegression(random_state=0)

#ekpaideysi
clf2.fit(X2_train,y2_train)

#provlepsi
y2_pred=clf2.predict(X2_test)

#ypologizoume to precision
#precision = precision_score(y2_test, y2_pred, average = 'micro')

#print('Precision: %.3f' % precision)







#efarmozoume decision tree

#input data
X3 = final_data[:,:5]

#output data
y3 = final_data[:,5]

lab_enc = preprocessing.LabelEncoder()

y3 = lab_enc.fit_transform ( y3 ) 


#diaspasi se train set kai test set 
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.20)


#dimiourgoume to montelo tou decision tree
clf3 = DecisionTreeClassifier(random_state=0)

#ekpaideysi
clf3.fit(X3_train,y3_train)

#provlepsi
y3_pred=clf3.predict(X3_test)

#ypologizoume to precision
#precision = precision_score(y3_test, y3_pred, average = 'micro')

#print('Precision: %.3f' % precision)











#efarmozoume SVM

#input data
X4 = final_data[:,:5]

#output data
y4 = final_data[:,5]

lab_enc = preprocessing.LabelEncoder()

y4 = lab_enc.fit_transform ( y4 ) 


#diaspasi se train set kai test set 
X4_train, X4_test, y4_train, y4_test = train_test_split(X4, y4, test_size=0.20)


#dimiourgoume to montelo tou SVM
clf4 = make_pipeline(StandardScaler(), SVC(gamma='auto'))

#ekpaideysi
clf4.fit(X4_train,y4_train)

#provlepsi
y4_pred=clf4.predict(X4_test)

#ypologizoume to precision
#precision = precision_score(y4_test, y4_pred, average = 'micro')

#print('Precision: %.3f' % precision)









#efarmozoume naive bayes

#input data
X5 = final_data[:,:5]

#output data
y5 = final_data[:,5]

lab_enc = preprocessing.LabelEncoder()

y5 = lab_enc.fit_transform ( y5 ) 


#diaspasi se train set kai test set 
X5_train, X5_test, y5_train, y5_test = train_test_split(X5, y5, test_size=0.20)


#dimiourgoume to montelo tou Naive Bayes
gnb = GaussianNB()

#ekpaideysi
gnb.fit(X5_train,y5_train)

#provlepsi
y5_pred=gnb.predict(X5_test)

#ypologizoume to precision
precision = precision_score(y4_test, y4_pred, average = 'micro')

print('Precision: %.3f' % precision)
