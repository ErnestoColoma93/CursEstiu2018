# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 09:08:14 2018

@author: tito-
"""

import pandas as pd

df = pd.read_csv("data/WHO.csv")

## mostrar df
df 
##
df.shape
df.columns

#### visualizacion de las columnas
for i , col in enumerate (df.columns): #**
    print ( i , col)
#####  
df.columns[10]

df.discribe()
df.tail(2)
type(df.columns)
df['Country']
type(df.Country)

fertilidad = df[df.columns[3]]
print (fertilidad.min())
print (fertilidad.max())
print (fertilidad.mean())
fertilidad.plot() 
df.plot()
print('suma de la fertilidad {}'.format(fertilidad.sum()))
################################################################

co2 = df["Total_CO2_emissions"]
print (co2.max())
row = df[df["Total_CO2_emissions"]==co2.max()]  # Esto es una condición dentro de la selección
################################################################
df.loc[0:1]
df.loc[0:1,['Continent']]
df.loc[0:1,["Continent","Total_CO2_emissions"]]

df.ix[0:4]

