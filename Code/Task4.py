#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:02:38 2019

@author: mridhoula
"""

import pandas as pd 
from pgmpy.estimators import HillClimbSearch
from pgmpy.estimators import K2Score
from pgmpy.models import BayesianModel


data = pd.read_csv("AND-Features.csv") 
hc = HillClimbSearch(data, scoring_method=K2Score(data))
best_model = hc.estimate()
print(best_model.edges())
k2=K2Score(data)
print('Best Model K2 Score: ' + str(k2.score(best_model)))
model1 = BayesianModel([('f1', 'f2'), ('f3', 'f4'),('f4', 'f6'), ('f6', 'f7'),('f2','f5'),('f1','f9'),('f9','f3'),('f9','f8')]) 
model2 = BayesianModel([('f4', 'f8'), ('f2', 'f8'),('f3', 'f1'), ('f9', 'f1'),('f7','f9'),('f4','f1'),('f6','f7'),('f5','f4')])  

print('Model 1 K2 Score: ' + str(k2.score(model1)))
print('Model 2 K2 Score: ' + str(k2.score(model2)))
