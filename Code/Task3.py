#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:43:43 2019

@author: mridhoula
"""

import csv
import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import  TabularCPD
from pgmpy.sampling import BayesianModelSampling
from pgmpy.estimators import HillClimbSearch
from pgmpy.estimators import K2Score





data=pd.read_csv('Table2.csv',delimiter=',')
mpd_1=(data[['x1 ( Relative)']])
a=np.array(mpd_1)
p1=TabularCPD("x1",4,a[0:4])


mpd_2=(data[['x2 (Shape of h loop)']])
b=np.array(mpd_2)
p2=TabularCPD("x2",5,b[0:5])


mpd_3=(data[['x3 (Shape of h arch)']])
c=np.array(mpd_3)
p3=TabularCPD("x3",3,c[0:3])

mpd_4=(data[['x4 (Height of Cross )']])
d=np.array(mpd_4)
p4=TabularCPD("x4",4,d[0:4])


mpd_5=(data[['x5 (Baseline of h)']])
e=np.array(mpd_5)
p5=TabularCPD("x5",4,e[0:4])

mpd_6=(data[['x6 (Shape of t)']])
f=np.array(mpd_6)
p6=TabularCPD("x6",5,f[0:5])




data2=pd.read_csv('Table3.csv',delimiter=',')
x_21=(data2.iloc[1:6, 1:])
g=np.array(x_21)
p_21=TabularCPD("x2",5,g[0:5],['x1'],[4])
x_41=(data2.iloc[6:10, 1:]) 
h=np.array(x_41)
p_41=TabularCPD("x4",4,h[0:4],['x1'],[4])
x_61=(data2.iloc[10:15, 1:]) 
i=np.array(x_61)
p_61=TabularCPD("x6",5,i[0:5],['x1'],[4])
data3=pd.read_csv('Table4.csv',delimiter=',')
x_32=(data3.iloc[1:4, 1:]) 
j=np.array(x_32)
p_32=TabularCPD("x3",3,j[0:3],['x2'],[5])
x_52=(data3.iloc[4:8, 1:]) 
k=np.array(x_52)
p_52=TabularCPD("x5",4,k[0:4],['x2'],[5])
data4=pd.read_csv('Table5.csv',delimiter=',')
x_23=(data4.iloc[1:6, 1:]) 
l=np.array(x_23)
p_23=TabularCPD("x2",4,l[0:4],['x3'],[3])
x_53=(data4.iloc[6:10, 1:]) 
m=np.array(x_53)
p_53=TabularCPD("x5",4,m[0:4],['x3'],[3])
x_63=(data4.iloc[10:15 ,1:]) 
n=np.array(x_63)
p_63=TabularCPD("x6",5,n[0:5],['x3'],[3])
data5=pd.read_csv('Table6.csv',delimiter=',')
x_14=(data5.iloc[1:5, 1:]) 
o=np.array(x_14)
p_14=TabularCPD("x1",4,o[0:4],['x4'],[4])
x_24=(data5.iloc[5:10, 1:]) 
p=np.array(x_24)
p_24=TabularCPD("x2",5,p[0:5],['x4'],[4])
x_64=(data5.iloc[10:15, 1:]) 
q=np.array(x_64)
p_64=TabularCPD("x6",5,q[0:5],['x4'],[4])
data6=pd.read_csv('Table7.csv',delimiter=',')
x_25=(data6.iloc[1:6, 1:])
r=np.array(x_25)
p_25=TabularCPD("x2",5,r[0:5],['x5'],[4])
x_35=(data6.iloc[6:10, 1:]) 
s=np.array(x_35)
p_35=TabularCPD("x35",3,s[0:3],['x5'],[4])
data7=pd.read_csv('Table8.csv',delimiter=',')
x_16=(data7.iloc[1:5, 1:]) 
t=np.array(x_16)
p_16=TabularCPD("x1",4,t[0:4],['x6'],[5])
x_26=(data7.iloc[5:10, 1:])
u=np.array(x_26)
p_26=TabularCPD("x2",5,u[0:5],['x6'],[5])
x_36=(data7.iloc[10:13, 1:]) 
v=np.array(x_36)
p_36=TabularCPD("x3",3,v[0:3],['x6'],[5])
x_46=(data7.iloc[13:17, 1:]) 
w=np.array(x_46)
p_46=TabularCPD("x4",4,w[0:4],['x6'],[5])

'''Best model is model2'''
model2 = BayesianModel([('x1', 'x2'),('x1', 'x6'),('x2','x5'),('x2','x3'),('x6','x4')])
model2.add_cpds(p1,p_21,p_52,p_32,p_46,p_61)
cpd1=[]
cpd1.append(p1)
cpd1.append(p_21)
cpd1.append(p_52)
cpd1.append(p_32)
cpd1.append(p_46)
cpd1.append(p_61)

model2.add_cpds(*cpd1)
'''generate data for model1'''
inference = BayesianModelSampling(model2)
data1=inference.forward_sample(size=3000, return_type='dataframe')
print("--------------------------------------------------")
'''Markov model'''
print("Coverting model2 to markov model:")
print("----------------------------------------")
mm=model2.to_markov_model()
print("Nodes of model2 as markov:")
print(mm.nodes())
print("Edges of model2 as markov:")
print(mm.edges())
print("----------------------------------------------")
print("Inference for th dataset")
from pgmpy.inference import VariableElimination
infer1 = VariableElimination(mm)
print("Inference of x4:")
print(infer1.query(['x4']) ['x4'])
print("Inference of x5|x2:")
print(infer1.query(['x5'], evidence={ 'x2': 1}) ['x5'])
print("---------------------------------------------------------")
print("AND DATASET")
data = pd.read_csv("AND-Features.csv") 
hc = HillClimbSearch(data, scoring_method=K2Score(data))
best_model = hc.estimate()
print("Edges of bayesian model")
print(best_model.edges())
'''Inference for and dataset'''
mm1=best_model.to_markov_model()
print("Edges of markov model")
print(mm1.edges())
print("Checking converted model:", mm1.check_model())
print("----------------------------------------------")
print("Inference for and dataset")
from pgmpy.inference import VariableElimination
infer2 = VariableElimination(mm1)
print(infer2.map_query(['f1','f9']))

