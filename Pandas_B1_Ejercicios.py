# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:36:16 2018
version Python 3.6.4 
@author: Ernesto Coloama Rotger 
"""
## Ejercicios Pandas Bloque 1 

import pandas as pd 

df = pd.read_csv('data/WHO.csv')


## 1) ¿Cuál es el país con mayor crecimiento urbano (“Urban_population_growth”)? 

grow = df['Urban_population_growth']
row3 = df[df["Urban_population_growth"]==grow.max()] 
print (row3['Country'].values[0])

## 2A) ¿Cuál es el país con menor crecimiento urbano?

row4 = df[df["Urban_population_growth"]==grow.min()]
print(row4['Country'].values[0])

## 2B) ¿Qué paises tienen un crecimiento urbano por encima 3.0?

row5 = df[df["Urban_population_growth"]>3.0]
print(row5['Country'])

## 3) ¿DESCRIBE las características de la fila: “Spain”?

rowS= df[df["Country"]== 'Spain']
rowS.describe()

## 4) ¿El continente donde está situado Spain es el mismo de UnitedStates?

c1=df[df['Country']=='United States of America']
c2 = df[df['Country']=='Spain']
c1['Continent'].values[0]== c2['Continent'].values[0]

## 5) ¿Cuáles son los cinco paises más contaminantes?

result = df.sort_values('Total_CO2_emissions', ascending=0)
result.head(5)

## 6) Observando algunas muestras del fichero puedes establecer la relación entre el identificador del continente y su nombre?

codigoContinentes = {1:"Asia",2:"Europa"} #Al menos hay 7!
print (codigoContinentes)

con1=df[df['Country']=='United States of America']
con1['Continent']
con2=df[df['Country']=='Australia']
con2['Continent']
con3=df[df['Country']=='India']
con3['Continent']
con4=df[df['Country']=='Argentina']
con4['Continent']
con5=df[df['Country']=='Rwanda']
con5['Continent']

codigoContinentes[int(con1['Continent'])]  = 'America del norte'
codigoContinentes[int(con2['Continent'])]  = 'Oceania'
codigoContinentes[int(con3['Continent'])]  = 'Asia menor'
codigoContinentes[int(con4['Continent'])]  = 'America del sur'
codigoContinentes[int(con5['Continent'])]  = 'Africa'

print (codigoContinentes)

##  7) Una vez identificado el nombre de los continentes, ¿puedes cambiar la columna de identificadores de continentes por sus respectivos nombres?

df.replace({'Continent': codigoContinentes },  inplace = True) ## Para mi una solucion mas sencilla y elegante 
df[0:10]

## 8) Puedes crear un nuevo dataframe con aquellos paises que sean de Europa.

df2 = df
df2 = df[df['Continent'] == "Europa"]
df2

## 9) ¿Cuáles son los paises más contaminantes de Europa?
## Propuesta A: usa el dataframe inicial

most_cont2=df.sort_values('Total_CO2_emissions',ascending=0)
most_cont2.head(10)

## Propuesta B: usa el dataframe de la actividad 8
most_cont=df2.sort_values('Total_CO2_emissions',ascending=0)
most_cont.head(10)

## 10) ¿Cuál es el continente con mayor número de paises?

canti = df.groupby(['Continent']).size()
canti




















