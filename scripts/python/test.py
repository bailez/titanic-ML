import pandas as pd
import numpy as np
import os
try:
    os.chdir(r'../../data/')
except FileNotFoundError:
    pass
# %% Read data
x = os.listdir()
rd = pd.read_csv
test ,train =  rd(x[0]), rd(x[1])
# %% Clean test data
df = test.drop(columns=['Name', 'Ticket','Cabin'])
df.Sex = df.Sex.map(lambda x: 0 if x == 'male' else 1) # 0 = male; 1 = female
df.Embarked = df.Embarked.map(lambda x: 0 if x ==  'Q' else( 1 if x == 'S' else 2))
df['Survived'] = np.nan
# %% Clean train data
train = train.drop(columns=['Name','Ticket','Cabin'])
train.Sex = train.Sex.map(lambda x: 0 if x == 'male' else 1)
train.Embarked = train.Embarked.map(lambda x: 0 if x ==  'Q' else( 1 if x == 'S' else 2))
# %% 
