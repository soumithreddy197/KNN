#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
from scipy import stats
from array import array
import os

test = open('Test.csv','r') 

testds = pd.read_csv(test)
k=5 

xtest=np.array(testds[testds.columns[0:48]])


'''
for line in testds : 
    testpoint = list(line)
    print(testpoint)
''' 

#diff= np.ones((1,xtrain.shape[0]))
result=[]
result.append(0)
result.append(1)
result[0]=[]
result[1]=[]
final=[]
final.append(0)
final.append(1)
final[0]=[]
final[1]=[]
testDict = dict()
Finalmode=[]
dictionary=dict()
for i in range(0,xtest.shape[0]): 
     result=[]
     result.append(0)
     result.append(1)
     result[0]=[]
     result[1]=[]
     dictionary[i]  = result
#print(xtrain[0,0:10]) 
#for i in range(0,xtest.shape[0]):
count=0
for line in sys.stdin :

    numbers = line.split(",")
    label=int(numbers[48])
    numbers=numbers[0:48]
    line = numbers  
    count=count+1
    #for line in sys.stdin :
    for i in range(0,xtest.shape[0]):
        result=[]
        result.append(0)
        result.append(1)
        result[0]=[]
        result[1]=[]
        final=[]
        final.append(0)
        final.append(1)
        final[0]=[]
        final[1]=[]       
        ct= list(xtest[i])      
        subli=[]
        for v in range(0,len(line)):
            subli.append(float(ct[v])-float(line[v]))
            subli[v]=subli[v]*subli[v]
        dist=sum(subli)

        if(count>k):
            maxi=max(dictionary[i][0])
            if(maxi>dist):
                maxipos=dictionary[i][0].index(max(dictionary[i][0]))
                dictionary[i][0][maxipos]=dist
                dictionary[i][1][maxipos]=label                
        else:
            dictionary[i][0].append(dist)
            dictionary[i][1].append(label)
        #dictionary[i] = result
for i in range(0,xtest.shape[0]) :    
    print("%s\t%s" % (i,dictionary[i]))




''' maxi=max(result[0])
    for j in range(0,k):
        minipos=result[0].index(min(result[0]))
        minilabel=result[1][minipos]
        final[0].append(minipos)
        final[1].append(minilabel)
        result[0][minipos]=maxi
    print(i,final)'''


'''
    #ct=np.transpose(np.dot(ct,diff))
    ED=np.square((xtrain-np.dot(ct,diff).transpose()))
    #ED=np.square(xtrain-np.tile(xtest[i],(xtrain.shape[0],1)))
    Identity=np.ones((ED.shape[1],1))
    ED=np.sqrt(np.dot(ED,Identity))
    Finalxtrain=np.append(xtrain,ED,axis=1)
    Finalxtrain=np.append(Finalxtrain,ytrain,axis=1)
    Finalxtrain=Finalxtrain[Finalxtrain[:,48].argsort()]
    counts = stats.mode(Finalxtrain[:k,49], axis = None)
    Finalmode.append(int(counts.mode))
    print('%s\t%s' %(i+1, Finalxtrain[:k,49]))
    #dictionary[i+1]=Finalxtrain[:k,49]
    #print('%s\t%s' %(i+1, Finalxtrain[:k,49]))

  '''     





