#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 00:21:34 2019

@author: mridhoula
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import numpy as np
''' x1,x2'''
with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    for j in range (1,5):
        
        for i in range(1,6):
       
           x=float(data[j][1])*float(data[i][2]);
          
           data1.append(x);
    
           
with open('Table3.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(2,7):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x1,x2:' , x)

    



'''x1 x4'''
with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    for j in range (1,5):
        
        for i in range(1,5):
       
           x=float(data[j][1])*float(data[i][4]);
          
           data1.append(x);
   
           
with open('Table3.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(7,11):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(16):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x1,x4:', x)



'''x1 x4'''
with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    for j in range (1,5):
        
        for i in range(1,6):
       
           x=float(data[j][1])*float(data[i][6]);
          
           data1.append(x);
    
           
with open('Table3.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(11,16):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
   
    
    
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x1,x6:' , x)


with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,6):
        
        for i in range(1,4):
       
           x=float(data[j][2])*float(data[i][3]);
          
           data1.append(x);
     
           
with open('Table4.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,6):
        for i in range(2,5):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(15):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x2,x3:' , x)




''' x2,x5'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,6):
        
        for i in range(1,5):
       
           x=float(data[j][2])*float(data[i][5]);
          
           data1.append(x);
    
           
with open('Table4.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,6):
        for i in range(5,9):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
   
    
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x2,x5:',  x)




''' x3,x2'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,4):
        
        for i in range(1,6):
       
           x=float(data[j][3])*float(data[i][2]);
          
           data1.append(x);
    
           
with open('Table5.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,4):
        for i in range(2,7):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(15):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x3,x2:',  x)


''' x3,x5'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,4):
        
        for i in range(1,5):
       
           x=float(data[j][3])*float(data[i][5]);
          
           data1.append(x);
     
           
with open('Table5.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,4):
        for i in range(7,11):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(12):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x3,x5:', x)




''' x3,x6'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,4):
        
        for i in range(1,6):
       
           x=float(data[j][3])*float(data[i][6]);
          
           data1.append(x);
      
           
with open('Table5.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,4):
        for i in range(11,16):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(15):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x3,x6:', x)




''' x4 x1'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,5):
        
        for i in range(1,5):
       
           x=float(data[j][4])*float(data[i][1]);
          
           data1.append(x);
     
           
with open('Table6.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(2,6):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
   
    
x=0.0
data3=[]
for i in range(16):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x4,x1:', x)


''' x4 x2'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,5):
        
        for i in range(1,6):
       
           x=float(data[j][4])*float(data[i][2]);
          
           data1.append(x);
    
           
with open('Table6.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(6,11):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
   
    
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x4,x2:', x)





''' x4 x6'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,5):
        
        for i in range(1,6):
       
           x=float(data[j][4])*float(data[i][6]);
          
           data1.append(x);
       
           
with open('Table6.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(11,16):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x4,x6:', x)


''' x5 x2'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,5):
        
        for i in range(1,6):
       
           x=float(data[j][5])*float(data[i][2]);
          
           data1.append(x);
    
           
with open('Table7.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(2,7):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
   
    
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x5,x2:',  x)






''' x5 x3'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,5):
        
        for i in range(1,4):
       
           x=float(data[j][5])*float(data[i][3]);
          
           data1.append(x);
     
           
with open('Table7.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,5):
        for i in range(7,10):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(12):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x5,x3:', x)

''' x6 x1'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,6):
        
        for i in range(1,5):
       
           x=float(data[j][6])*float(data[i][1]);
          
           data1.append(x);
  
           
with open('Table8.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,6):
        for i in range(2,6):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
   
    
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x6,x1:', x)



''' x6 x2'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,6):
        
        for i in range(1,6):
       
           x=float(data[j][6])*float(data[i][2]);
          
           data1.append(x);
     
           
with open('Table8.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,6):
        for i in range(6,11):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(25):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x6,x2:', x)



''' x6 x3'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,6):
        
        for i in range(1,4):
       
           x=float(data[j][6])*float(data[i][3]);
          
           data1.append(x);
    
           
with open('Table8.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,6):
        for i in range(11,14):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
    
    
x=0.0
data3=[]
for i in range(15):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x6,x3:', x)



''' x6 x4'''

with open('Table2.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]
    data1=[]
    
    
    for j in range (1,6):
        
        for i in range(1,5):
       
           x=float(data[j][6])*float(data[i][4]);
          
           data1.append(x);
    
with open('Table8.csv', mode='r') as f:
    reader= csv.reader(f)
    data= [row for row in reader]           
    data2=[]
    j=1
    for j in range(1,6):
        for i in range(14,18):
           
           x=float(data[1][j])*float(data[i][j])
           data2.append(x);
    
     
x=0.0
data3=[]
for i in range(20):
    y= abs(data2[i]-data1[i])
    x=x+y
print(' x6,x4:', x)

