#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:25:07 2022

@author: mkc
"""

# %%%   Matplotlip

# Line Plot, Scatter Plot, Bar Plot, Subplots, Histogram

import pandas as pd

df=pd.read_csv("iris.csv")

print(df.columns)

print(df.Species)

print(df.Species.unique())

print(df.info())

print(df.describe())

setosa= df[df.Species == "Iris-setosa"]

versicolor= df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())


# %%   Line Plot


import matplotlib.pyplot as plt


df1=df.drop(["Id"],axis=1)

df1.plot()
plt.show()


setosa= df[df.Species == "Iris-setosa"]

versicolor= df[df.Species == "Iris-versicolor"]

virginica= df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm, color="red", label="setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color="green", label="versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm, color="blue", label="virginica")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid=True)
plt.show()


df1.plot(grid=True,linestyle=":")
plt.show()

df1.plot(grid=True,alpha=0.2)
plt.show()


# %%   Scatter Plot



setosa= df[df.Species == "Iris-setosa"]
versicolor= df[df.Species == "Iris-versicolor"]
virginica= df[df.Species == "Iris-virginica"]


plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color="red", label="setosa")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color="blue", label="virginica")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color="green", label="versicolor")

plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.legend()
plt.title("scatter plot")
plt.show()



# %%   Histogram



plt.hist(setosa.PetalLengthCm, bins=10)
plt.xlabel("PetalLengthCm")
plt.ylabel("Frekans")
plt.title("histogram")
plt.show()


# %%   Bar plot



import numpy as np

x=np.array([1,2,3,4,5,6,7])
a=["Turkey","usa","e","r","t","s","f"]
y=x*2+5

plt.bar(a,y) # pltbar(x,y)
plt.title("bar plot")
plt.xlabel(x)
plt.ylabel(y)
plt.show()


# %%   Subplot


df1.plot(grid=True,alpha=0.5,subplots=True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.show()




