#Python solution using decision tree
from utils import get_data
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier


train, test = get_data()
# %% Concatenate train and test data into a df
#reg = LinearRegression()
clf = DecisionTreeClassifier()
clf.fit(train.drop(columns=['Survived']),train.Survived)
print(clf.score(train.drop(columns=['Survived']), train.Survived))
# %% Make prediction and transform in logistic
prediction = clf.predict(test)
prediction = pd.Series(prediction).apply(lambda x: 0 if x<0.5 else 1)
# %% Create Dataframe for submission
output = {'PassengerId' : test.PassengerId, 'Survived': prediction}
df = pd.DataFrame(output)
# %%
print(df)
os.chdir(r'../submissions')
df.to_csv('tree-py.csv', index=False)