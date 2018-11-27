#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:41:34 2018

@author: lv
"""

# Importação das bibliotecas 
import numpy as np
import pandas as pd

# Leitura dos dados em formato ".csv"
data       = pd.read_csv('mg_data.csv', delimiter=' ', header=None).values
data       = data.T

# Separação dos conjuntos treino/teste
u       = data[:,0:1000]
u_test  = data[:,1000:]

# Inicialização das matrizes
tam       = max(u.shape)

Z         = np.zeros([tam,tam],dtype=object) # Centro dos clusters
P_centers = np.zeros([tam,tam],dtype=object) # Pontencial dos centros de clusters (P(z))
P_in      = np.zeros([tam,tam],dtype=object) # Potencial dos dados de entrada
Vk        = np.zeros([1,tam],dtype=object)   # 
Qk        = np.zeros([1,tam],dtype=object)   # 
Lk        = np.zeros([1,tam],dtype=object)   # 
Phik      = np.zeros([1,tam],dtype=object)   # 
Theta     = np.zeros([tam,tam],dtype=object) # 
Pi        = np.zeros([tam,tam],dtype=object) #

# Inicialização do algoritmo 
Z[0,0] = u[:,0]
P_centers[0,0] = 1
P_in[0,0] = 1
R = 1

# Calculo do potencial dos dados de entrada
for k in range(1,tam):
    
    Vk[0,k]   = (np.linalg.norm(u[:,k]))**2
    
    Qk[0,k]   = (Qk[0,k-1]) + (np.linalg.norm(u[:,k]))**2
    
    Phik[0,k] = (Phik[0,k-1]) + u[:,k-1]
    
    Lk[0,k]   = (Phik[0,k])*(u[:,k])
        
    P_in[0,k] = ((1 + Vk[0,k] + ((Qk[0,k]-2*Lk[0,k])/(k-1)))**-1)
    
    
    # Atualização do potencial de cada centro (eq 2.10)
    for i in range(1,R+1):
        
        P_centers[i,k] = (((k-1)*(P_centers[i,k-1]))/(k-2+(P_centers[i,k-1])*(1+(np.linalg.norm(Z[i,k]-Z[i,k-1]))**2)))
    
    # Condição de substituição
    if P_in[0,k] > P_centers[k].max() :
        
        if ((P_in[0,k])/(P_centers[k].max())) - 
        






