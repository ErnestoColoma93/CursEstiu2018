
"""
Created on Thu Jul 19 12:12:03 2018
version : 3.6.4 
@author: Ernesto Coloma Rotger 

"""
import pandas as pd 
import numpy as np
df= pd.read_csv("data/WHO.csv")

## Ejercicion Pandas Bloque 5 

# 1) Si en el último ejemplo hemos visualizado los paises más contaminantes, podrías hacer lo mismo con los 10 paises menos contaminantes.

co2 = df["Total_CO2_emissions"].sort_values(ascending=True).head(10) 
dateSelect = df.loc[co2.index] 
co2.index = dateSelect["Country"] 
ax = co2.plot(kind="bar")
ax.set_title("Paises menos contaminantes del mundo")

# 2) Representa en un gráfico de columnas el crecimiento de población del “top 10” de países contaminantes.

co3 = df["Total_CO2_emissions" ].sort_values(ascending=False).head(10)
grow = df.Population_growth[co3.index]
dateSelect = df.loc[grow.index]
grow.index = dateSelect["Country"] ###
ax = grow.plot(kind="bar")###
ax.set_title("Crecimiento de la poblecion en los apises menos contaminantes del mundo")

# 3) Representa en un gráfico de columnas el crecimiento de población del “top 10” de países menos contaminantes.

co4 = df["Total_CO2_emissions" ].sort_values(ascending= True).head(10)
growl = df.Population_growth[co4.index]
dateSelect = df.loc[growl.index]
growl.index = dateSelect["Country"] 
ax = growl.plot(kind="bar")

## 4) Representa con un boxplot la contaminación (CO2) de cada continente

continents = {1: 'Asia', 2: 'Europa', 4: 'America del norte', 6: 'Oceania', 7: 'Asia menor', 5: 'America del sur', 3: 'Africa'}
df.replace({'Continent': continents },  inplace = True)
df.dropna(subset=['Total_CO2_emissions'])
ax = df.boxplot(by='Continent', 
                       column=['Total_CO2_emissions'], 
                       grid=False,figsize=(20,10))

## 5) Con los tres dataframes (empleado,salario,encuesta): Crea una gráfica para visualizar que empleados tienen mayor salario

dff = pd.read_csv('data/FIN.csv')## importado del bloque anterior el dataframe ya filtrado 

sal = dff.groupby('Nombres').agg({'Salario':np.sum})

sal.plot(kind= 'bar')

## 6) En Campus Extens, hay un fichero CSV sobre información del Titanic. Visualiza con un pastel cuantos fueron los que sobrevivieron vs los que murieron

tit = pd.read_csv('data/titanic3.csv')
tit.head() # miramos la froma de los datos 
tit.shape
tit2 = tit.replace({'survived':{0 :"Muerto ",1:"Superviviente "}})
graf =tit2["survived"].value_counts().plot(kind="pie")

##7) Haz la visualización anterior por barras, desglosando hombres/mujeres

barra = tit[['survived','sex']].groupby('sex').sum().plot(kind='bar')
barra.set_xticklabels(["Hombre","Mujer"])

#8) Lo mismo, pero teniendo en cuenta la edad¶

tit[['survived','age']].groupby('age').sum().plot(kind='bar',figsize=(20,10))


