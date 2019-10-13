#Python solution using ordinary least squares model
import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
try:
    os.chdir(r'../../data/')
except FileNotFoundError:
    pass
# %% Read data
x = os.listdir()
rd = pd.read_csv
test ,train =  rd(x[0]), rd(x[1])
# %% Clean test data
test = test.drop(columns=['Name', 'Ticket','Cabin'])
test.Sex = test.Sex.map(lambda x: 0 if x == 'male' else 1) # 0 = male; 1 = female
test.Embarked = test.Embarked.map(lambda x: 0 if x ==  'Q' else( 1 if x == 'S' else 2))
test.Age = test.Age.fillna(29)
test.Fare = test.Fare.fillna(36)
# %% Clean train data
train = train.drop(columns=['Name','Ticket','Cabin'])
train.Sex = train.Sex.map(lambda x: 0 if x == 'male' else 1)
train.Age =  train.Age.fillna(28)
train.Embarked = train.Embarked.map(lambda x: 0 if x ==  'Q' else( 1 if x == 'S' else 2))
# %% Concatenate train and test data into a df
reg = LinearRegression()
reg.fit(train.drop(columns=['Survived']),train.Survived)
print(reg.score(train.drop(columns=['Survived']), train.Survived))
# %% Make prediction and transform in logistic
prediction = reg.predict(test)
prediction = pd.Series(prediction).apply(lambda x: 0 if x<0.5 else 1)
# %% Create Dataframe for submission
output = {'PassengerId' : test.PassengerId, 'Survived': prediction}
df = pd.DataFrame(output)
# %%
os.chdir(r'../submissions')
df.to_csv('ols-py.csv')