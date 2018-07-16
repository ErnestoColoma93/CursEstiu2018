# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:57:44 2018
version Python 3.6.4
@author: Ernesto Coloma 

"""

## Ejercicion Pandas_B3 
import pandas as pd
from pandas import HDFStore,DataFrame
import numpy as np

'''
1) Usando el fichero WHO.csv, ¿Cuál es el volumen total de CO2 emitido por cada continente?
'''
continents = {1: 'Asia', 2: 'Europa', 4: 'America del norte', 6: 'Oceania', 7: 'Asia menor', 5: 'America del sur', 3: 'Africa'}
df2 = pd.read_csv("data/WHO.csv")
df2.replace({'Continent': continents },  inplace = True)
gro = df2.groupby("Continent").agg({"Total_CO2_emissions":np.sum})
print (gro)

'''
2) ¿Cuál es el número de paises por continente?
'''
gro2 = df2.groupby("Continent").agg({"Country":np.size})
print (gro2)

'''
3) Carga el fichero climaMallorca.csv: ¿Cual es la temperatura máxima cuando el viento es inferior a 10? ¿Cuántas muestras hay?
'''
Cm = pd.read_csv('data/climaMallorca.csv')

cm2 = Cm.sort_values( by=['temperature_mean'] ,ascending=False )

cm3 = cm2[cm2['wind'] < 10 ]

print (cm3.head())
print (cm3.shape)

'''
4) ¿Cual es la temperatura máxima cuando el viento es inferior a 10 y superior a 20? ¿Cuántas muestras hay?
'''

x1 = cm2.query( 'wind not in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]').agg(({'temperature_mean':'max'}))[0]
print ( 'La temperatura maxima fue {}'.format(x1))
x2 = cm2.query( 'wind not in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]').count()[0]
print ('El tamaño de la muestra es: {}'.format(x2))

'''
5) Selecciona al azar: 30 paises y calcula la media de "Net primary school enrolment ratio female (%)" agrupado por Continente
Nota: la selección de 30 paises se basa en la creación de un indice.
'''
df2 = df2.sample(frac=1, random_state=42)
df_30 = df2.loc[:30]
x4 = df_30['Net primary school enrolment ratio female (%)'].mean()
print (x4)

''''
6) Repite la anterior actividad pero ahroa con todos los paises. ¿Sale la misma media?
'''

df2['Net primary school enrolment ratio female (%)'].mean()
# Mury parecida pero no la misma 

'''
7) Repasemos: Guarda el fichero WHO.csv en un fichero HDF5
'''
dff = pd.read_csv('data/WHO.csv')
# este apartado da un erro de 'ValueError' ya qeu hay varias  columnas que en el nombre tiene un caracter no permitido en fomato HDFS, asi que renombramos las problematicas
dff.rename(columns={'Deaths among children under five years of age due to HIV/AIDS (%)':'Deaths among children under five years of age due to AIDS (%)',
                    'Deaths due to HIV/AIDS (per 100 000 population per year)':'Deaths due to AIDS (per 100 000 population per year)' },
                       inplace=True)


hdf = HDFStore('data/storageddd.h5')
hdf.put('DD', dff, format='table', data_columns=True)















