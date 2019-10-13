import pandas as pd
import os

try:
    os.chdir(r'../../data/')
except FileNotFoundError:
    pass

# %% Cleanse data
x = os.listdir()
rd = pd.read_csv
test ,train =  rd(x[0]), rd(x[1])
df = test.drop(columns=['Name', 'Ticket','Cabin'])
df.Sex = df.Sex.map(lambda x: 0 if x == 'male' else 1) # 0 = male; 1 = female
df.Embarked = df.Embarked.map(lambda x: 0 if x ==  'Q' else( 1 if x == 'S' else 2))

