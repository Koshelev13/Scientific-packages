import numpy as np
import pandas as pd
data = pd.read_csv('titanic.csv')
pd.pivot_table(data[["Sex", "Survived"]],
index = ["Sex"],
columns = ["Survived"],
aggfunc = len)
print(data.isnull().sum())
group = pd.DataFrame(data, columns=['SibSp', 'Parch'])
data['Relatives'] = data[['SibSp','Parch']].sum(axis=1)
group = pd.DataFrame(data, columns=['SibSp', 'Parch'])
data['Relatives'] = group.any(axis = 1)
group = pd.DataFrame(data, columns=['SibSp', 'Parch', 'Relatives'])
print(group)
male = data['Sex'].value_counts()
print(male)
data.loc[(data['Pclass'] == 1), 'Pclass'] = 'elite'
data.loc[(data['Pclass'] == 2), 'Pclass'] = 'middle'
data.loc[(data['Pclass'] == 3), 'Pclass'] = 'redneck'
print(data['Pclass'])
data['Fare_bin'] = data['Fare']
data.loc[(data['Fare'] < 20), 'Fare_bin'] = 'Дешево'
data.loc[(data['Fare'] >= 20), 'Fare_bin'] = 'Дорого'
print(data['Fare_bin'])
print(data['Fare_bin'].value_counts())
data = data.assign(Expensive = list([0] * data.shape[0]))
data.loc[(data.Fare >= 20), 'Expensive'] = 1
pd.pivot_table(data[["Expensive", "Survived"]],
index = ["Expensive"],
columns = ["Survived"],
aggfunc = len)
print(data)