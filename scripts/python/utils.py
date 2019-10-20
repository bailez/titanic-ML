import pandas as pd
import os

def get_data():
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
    return train, test