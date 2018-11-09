#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:41:34 2018

@author: lv
"""

# Importação das bibliotecas 
import numpy as np
import pandas as pd

# Leitura do dataset em formato ".csv"
u = pd.read_csv('mg_data.csv', delimiter=' ', header=None)
u = u.T

# Inicialização das matrizes Z e P, de Vk, Qk e Lk
Z = pd.DataFrame(np.zeros((1000, 1201),dtype=object))
P_centers = pd.DataFrame(np.zeros((1000, 1201),dtype=object))
P_in = pd.DataFrame(np.zeros((1000, 1201),dtype=object))
Vk = pd.DataFrame(np.zeros((1, 1201),dtype=object))
Qk = pd.DataFrame(np.zeros((1, 1201),dtype=object))
Lk = pd.DataFrame(np.zeros((1, 1201),dtype=object))
Phik = pd.DataFrame(np.zeros((1, 1201),dtype=object))

tam = max(u.shape)


# Inicialização do algoritmo 
Z.iloc[0][0] = u.iloc[:][0]
P_centers.iloc[0][0] = 1
P_in.iloc[0][0] = 1
R = 1


# Primeiro for (k)
for k in range(tam+1):
    Vk.iloc[0][k+1] = (np.linalg.norm(u.iloc[:][k+1]))**2
    
    Qk.iloc[0][k+1] = (Qk.iloc[0][(k+1)-1]) + (np.linalg.norm(u.iloc[:][k+1]))**2
    
    Phik.iloc[0][k+1] = (Phik.iloc[0][(k+1)-1]) + u.iloc[:][(k+1)-1]
    
    Lk.iloc[0][k+1] = (Phik.iloc[0][k+1])*(u.iloc[:][k+1])
    
    P_in.iloc[0][k+1] = ((1 + Vk.iloc[0][k+1] + ((Qk.iloc[0][k+1]-2*Lk.iloc[0][k+1])/((k+1)-1)))**-1)
    
    
    #Equação (2.10)
    for i in range(R+1):
        P_centers.iloc[i+1][k+1] = ((((k+1)-1)*P_centers.iloc[i+1][(k+1)-1])/((k+1)-2+P_centers.iloc[i+1][(k+1)-1]*
                      (1+(np.linalg.norm(Z.iloc[i+1][k+1] - Z.iloc[i+1][(k+1)-1]))**2)))
    
    
    # Condição de substituição 
    if P_in.iloc[0][k+1] > P_centers[k+1].max() :
        
        if #segunda condição 2.12


        
        
        
# Teste de versão do git.    





