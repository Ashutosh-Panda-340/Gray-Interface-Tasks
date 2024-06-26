# -*- coding: utf-8 -*-
"""sonu_task_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xQLyLhR2BFN44HInJ2yHk_r9WVW3z-kR
"""

import pandas as pd

import numpy as np

df = pd.read_csv("sonu_2347015_tasks\cereal.csv")

df.head()

#Question2
a=df[df['calories']<=70].index
print(f"indexes of rows in which calories are less than 70 are {a}")

b=df[df['protein']>=4].index
print(f"indexes of rows in which protein is greater than 4 are {b}")

#Question3
c=df[df['fat']==1].index
print(c)
df.drop(c, inplace=True)

df.head()

#Question1
d=df['name'].str.split(" ", expand=True)
print(d)

#printing only part of it
print(d[1])

