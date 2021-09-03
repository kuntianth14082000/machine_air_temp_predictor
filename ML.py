import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge,Lasso ,RidgeCV,LassoCV , ElasticNet , ElasticNetCV,LinearRegression

### Importing Required dataset
df=pd.read_csv('ai4i2020.csv')

#Drop unwanted columns
df.drop(columns=['UDI','Product ID','Type'],inplace=True)

### Spliting Independent and Dependent dataset
x=df.drop(columns=['Air temperature [K]'])
y=df['Air temperature [K]']

### Performing standardisation on the dataset to scale down the data
scaler=StandardScaler()
arr=scaler.fit_transform(x)
df1=pd.DataFrame(arr)

### Spilt training and testing dataset
x_train,x_test,y_train,y_test=train_test_split(arr,y,test_size=0.15,random_state=345)

### Training Model
lr=LinearRegression()
lr.fit(x_train,y_train)

def pred(d):
    #predicting values
    '''
    l=[]
    for i in d.values():
        l.append(i)
    a=lr.predict([l])'''

    b=[['-0.947360','0.068185','0.282200','-1.695984','-0.187322','-0.06798','-0.10786','-0.097934','-0.099484','-0.04363']]
    b=lr.predict(b)
    return b

#b=[['-0.947360','0.068185','0.282200','-1.695984','-0.187322','-0.06798','-0.10786','-0.097934','-0.099484','-0.04363']]
#b=pred(b)
#print(b)