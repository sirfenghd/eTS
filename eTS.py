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

# Inicialização das matrizes Z e P 
Z = pd.DataFrame(np.zeros((1000, 1200),dtype=object))
P_center = pd.DataFrame(np.zeros((1000, 1200),dtype=object))
P_in = pd.DataFrame(np.zeros((1000, 1200),dtype=object))

tam = max(u.shape)


# Inicialização do algoritmo 
Z.iloc[0][0] = u.iloc[:][0]
P_center.iloc[0][0] = 1
R = 1

# print(Z.iloc[0][0][0]) print de teste


# Primeiro for
#for k in range(tam):









