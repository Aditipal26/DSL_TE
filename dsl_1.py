# -*- coding: utf-8 -*-
"""DSL-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mgv5awCdtXVDRatkeYGjvg4Fhuqa2FwA
"""

import pandas as pd
df = pd.read_csv('/content/tested (2).csv')
df

df.loc[2]

df.head(5)

df.tail(5)

df.info(3)

ser = pd.Series({"PassengerId": 60, "Survived": 13, "Pclass": 26, "Name": "Aditi", "Sex": "Female", "Age": 20, "SibSp": 1, "Parch": 67, "Ticket": 4, "Fare": 200, "Cabin": "Lab", "Embarked": "Totally"})
print(ser)

df.isnull()

df.shape

import pandas as pd
df = pd.read_csv('/content/airquality.csv')
df

df.isnull().sum()