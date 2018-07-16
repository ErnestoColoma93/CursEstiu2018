# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:15:59 2018
version Python 3.6.4 
@author: Ernesto Coloma

"""
## Ejercicios Pandas Bloque 2
import string
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
import time 
from pandas import read_hdf

'''

1) Crea un dataframe con al menos 4 series de 100 elementos:
Las series son las siguientes:

    name : Distribución aleatoria de 8 characteres
    km2 : Distribución aleatoria entre 10-100
    age : Distribución normal entre 1-90, el valor medio a vuestro gusto
    level: Distribución aleatoria de cuatro grados: none, school, high, university

'''

#creamos los datos 

df2 = pd.DataFrame()
name=[]
for n in range (100):        
        a = np.random.choice(list(string.ascii_uppercase),8)
        na = ''.join(a)
        name.append(na)
        
name 
## km cuadrados
km2 = []
for n in range(100):
    a = np.random.randint(10,100)
    km2.append(a)
km2
## edad 
edad = list(np.random.normal(50 , 20 , 100))
edad

## level 
grados = ['none', 'school', 'high', 'university']
level = []
for n in range(100):
    a= np.random.choice(grados)
    level.append(a)
level 

## creamos el dataframe 
df1 = pd.DataFrame() 
df1['name']  = name
df1['km2'] = km2
df1 ['age'] = edad
df1 ['level'] = level

'''
2) Guarda el dataframe en un fichero CSV. ¿Cuánto espacio ocupa?. ¿Puedes abrirlo en excel?
'''   
df1.to_csv('data/export.csv')

# ocupa 5 Kb , se puede abir con excel pero se ve en formato CSV     

'''
3) Guarda el dataframe anterior en una fichero HDF5. ¿Cuánto espacio ocupa? ¿Puedes abrirlo en un excel?    
'''    

hdf = HDFStore('data/storage_exper.h5')
hdf.put('D1', df1, format='table', data_columns=True)
## ocuapa 72 Kb y no lo podemos abrir con el excel     
    
'''
4) Crea un nuevo dataframe con las columnas: age y level, donde level == none. ¿Cuántos campos hay?
'''
df2 = df1[["age","level"]]
df3 = df2[df2['level']=='none']
df3   

'''
5) Guarda del ejercicio 4, en el mismo HDF5, con otro key
'''

hdf.put('D2', df3, format='table', data_columns=True)

''' 
6) En un nuevo dataframe, carga del fichero HDF5 -el df del ejercicio 4- con age por encima de los 40 años   
'''

df4 = read_hdf('data/storage_exper.h5', 'D2', 'a' , where=['age > 40'] )
print (df4)

'''
7) Repite el paso 2 y 3 pero está vez mirando cuanto tiempo tardas en hacer una operación de escritura (CSV,HDF5) y de carga de ambos dataframes.
'''

# Tiempo guardado en un csv 
dff=DataFrame()
start = time.clock()
df1.to_csv('data/export.csv')
end = time.clock()
print ("Tiempo necesitado de escritura: {}" .format(end-start))
# Tiempo de carfga 
start = time.clock()
dff = pd.read_csv('data/export.csv')
end = time.clock()
print ("Tiempo necesitado de carga: {}" .format(end-start))

# Tiempo guardado en un csv 
start = time.clock()
hdf = HDFStore('data/storage_exper.h5')
hdf.put('D1', df1, format='table', data_columns=True)
end = time.clock()
print ("Tiempo necesitado: {}" .format(end-start))
# Tiempo de carfga 
start = time.clock()
df4 = read_hdf('data/storage_exper.h5', 'D1', 'a' )
end = time.clock()
print ("Tiempo necesitado de carga: {}" .format(end-start))

## podemos observar que requeire mas tiempo tanto para la lectura como para la escritura el formato HDF5

    
    