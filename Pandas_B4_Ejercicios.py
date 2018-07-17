# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 00:53:01 2018
version Python 3.6.4
@author: Ernesto Coloma Rotger
"""

'''
Ejercicios de gestión de valores perdido
'''

import pandas as pd 
import numpy as np
import string

#  1) Del fichero who.csv, contabiliza cuántos paises tienen algun valor NaN.


df = pd.read_csv("data/who.csv")

df.isnull().any(axis=1).sum()

# 1b) Ordena el anterior resultado para identificar cuál es el pais con mayor número de campos desconocidos 

df2 = df.isnull().sum(axis=1).sort_values(ascending = False ).index

pais = df.Country.loc[int(df2[0])]

print( ' El pais con mas valores nulos es {}'.format(pais))

# 2) who.csv, Selecciona la primera, tercera y decima columna, de las filas comprendidas entre la 100 y la 150. 

df3 = df[[df.columns[0],df.columns[2],df.columns[9]]][100:150]
df3.shape

#2b) ¿Cuántos valores NaN hay presentes?

df3.isna().sum().sum()

# 2c) Crea un nuevo dataframe donde los NaN sean cero

df4 = df3.fillna(0)


# 2d) Elimina aquellas filas de la anterior selección donde haya NaN

df5 = df3.dropna(axis=0)

# 3) Genera un dataframe de 5 x 100, con números aleatorios entre 0-10. Las celdas que superen un valor de >=8 se conviertan en valores NaN

dfra = pd.DataFrame( {'dump' : np.random.randint(0 ,10 ,size = 100 ) , 
                      'dump2' :np.random.randint(0 ,10,size = 100 ),
                      'dump3':np.random.randint(0 ,10, size = 100 ),
                      'dump4 ': np.random.randint(0 ,10, size = 100 ),
                     'dump5': np.random.randint(0 ,10, size = 100 )
                     })
dfra[dfra >= 8]=np.nan
dfra.shape # comprovamos que tiene la forma correcta 

# 3a) Interpola los anteriores valores mediante interpolación simple

dfra.interpolate()

#3b) Interpola la serie 3, hasta un limite de 10 interpolaciones, con el metodo del más cercano "nearest"

dfra.dump3.interpolate(method='nearest' , limit= 10 )

'''
Ejercicios de agrupaciones
Configuración del gran ejercicio...

Crea tres dataframes:

    DF_EMP: El primero estará formado por empleados. Columns= DNI, Nombre, Apellidos, Categoria. SHAPE(4x30) Valores aleatorios!
    DF_SAL: El segundo contendrá el salario. Columns=selecciona valores de la columna del DNI, Salario. SHAPE(2X30). Puede darse el caso de personas que tengan más de un salario.
    DF_ENQ: El tercero contendrá encuestas. Columns= selecciona valores aleatorios de la columna Apellido, R1, R2, R3 (Ri son columnas con valores enteros entre 0-10). Shape(4x100). Coge 20 celdas aletorias de Respuestas y asignalas el valor np.NaN

'''
####### Creacion de los tres dataframes 
# DNI
DNI = []
DNI1 = []
for  n in range (30 ):
    x = np.random.choice(['0','1','2','3','4','5','6','7','8','9'],8)
    a = ''.join(x)
    DNI.append(a)
    
for n in DNI :
    b = np.random.choice(list(string.ascii_uppercase),1)
    c = ''.join(b)
    y = n + c 
    DNI1.append(y)
DNI1

# Nombres 
nom=[]
for n in range (30):        
        a = np.random.choice(list(string.ascii_uppercase),8)
        na = ''.join(a)
        
        nom.append(na)
#Apellidos 

apell = []
for n in range (30):        
        a = np.random.choice(list(string.ascii_uppercase),8)
        na = ''.join(a)
        apell.append(na)

#Categoria
cat = []
for n in range (30):        
        a = np.random.choice(list(string.ascii_uppercase),3)
        na = ''.join(a)
        cat.append(na)
# Creamos DF_EMP
DF_EMP = pd.DataFrame({'DNI':DNI1 , 'Nombres': nom , 'Apellidos': apell, 'Categorias':cat})

# Salario 
sal = np.random.randint(0, high=100001 , size = 30)

# DNI_Sal
DNI_Sal = []
for n in range (30):
    a = str (np.random.choice(DNI1))
    DNI_Sal.append(a)
    

#Creamos DF_SAL

DF_SAL = pd.DataFrame({'DNI':DNI_Sal,'Salario':sal})


# Enceuntas 
apell_en = []
for n in range (100):
    a = list (np.random.choice(apell,1))
    
    apell_en.append(a[0])
     

# Ri
r1 = list(np.random.randint(0,11,size=100))
r2 = list(np.random.randint(0,11,size=100))
r3 = list(np.random.randint(0,11,size=100))

# Creamos DF_ENQ y asignamos 20 NaN al azar 

DF_ENQ = pd.DataFrame({'Apellidos':apell_en, 'R1':r1 , 'R2':r2 , 'R3':r3})
while (pd.isnull(DF_ENQ).sum().sum() != 20): 
    x = np.random.randint(1 ,4)
    y = np.random.randint( 0 , 100)
    DF_ENQ.iloc[y, x] = np.NAN

####

#4) Crea un dataframe con aquellos empleados que ganen más de un valor umbral del salario. Tú decides el valor del umbral.    

df1 =DF_SAL[DF_SAL.Salario > 45000]

# 5) Crea un dataframe con aquellos empleados que ganen menos de un valor umbral del salario. Tú decides el valor del umbral.

df2 =DF_SAL[DF_SAL.Salario <= 45000]

# 6) Concadena los dataframes del punto 4 y 5

df3 = pd.concat([df1, df2], axis=0)

# 7) ¿Cuántas personas no tienen salario?

x1 = list(DF_SAL.DNI) 
x2  = list(DF_EMP.DNI) 
cont = 0
for n in x2 :
    if((n not in x1) == False ):
        cont +=1
print ( 'Los empleados sin salario son : {}'.format(cont))

# 8) ¿Crea un dataframe uniendo las tablas de Empleado y Salario? Descarta a empleados que no tengan salario.
        
uni = pd.merge(DF_EMP, DF_SAL, on = 'DNI')

# 9) ¿Cuál es la frecuencia de participacipn de una persona en las encuestas?

DF_ENQ.groupby('Apellidos').size()

# 10) ¿Cuál es la Ri con mejor participación?

Ri = DF_ENQ.isnull().sum(axis=0).sort_values(ascending = True ).index
print ('El cuestionario con mejor participacion es el {}'.format(Ri[1]))

#11) ¿Cuál es la persona con valoraciones más bajas?

maxi = DF_ENQ.sum(axis=1).sort_values(ascending= True).index
print (DF_ENQ.iloc[maxi[0] ])

#12) FUSIONA las tres tablas en función del DNI y Apellido! Elimina aquellas personas que no tengan ni salario ni encuestas.

uni1 = pd.merge(DF_EMP, DF_SAL , how='left',on='DNI')
uni11 = uni1.dropna(axis=0) # los unicos valores nulos seran los de salario, portanto se eliminaran
uni2 = pd.merge(uni11, DF_ENQ , how='left', on = 'Apellidos')
fin = uni2.dropna(axis=0,thresh=3,subset=['R1','R2','R3'])## solo con los tres cuationarios sin contestar 
fin 