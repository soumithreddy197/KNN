#!/usr/bin/env python3
'''
#!/usr/bin/env python3
from operator import itemgetter
import sys
import pandas as pd
import numpy as np
from scipy import stats
from array import array

i=0
word=None
Finalmode=[]
for line in sys.stdin:
	i+=1
	line=line.strip()
	word,Finalxtrain=line.split('\t',1)
        
	Finalxtrain=np.asarray(Finalxtrain)
	counts = stats.mode(Finalxtrain)
	Finalmode.append(int(counts.mode))

	print('%s\t%s' %(i, Finalmode))
''' 
'''
import sys
from statistics import mode

for line in sys.stdin:
    print(line)

'''
import sys
#from statistics import mode
from scipy import stats
import ast 
total=[]
total.append(0)
total.append(1)
total[0]=[]
total[1]=[]
k =5
current_key =None 
for line in sys.stdin:
    line = line.strip()
    key, at = line.split("\t", 1)
    try :
        at = ast.literal_eval(at)
    except ValueError: 
        continue
    if current_key == key:
        total[0]=total[0]+at[0]
        total[1]=total[1]+at[1]
    else : 
        if current_key :
            label = []
            maxi=max(total[0])
            for i in range(0,k):
                minipos=total[0].index(min(total[0]))
                minilabel=total[1][minipos]
                label.append(minilabel)
                total[0][minipos]=maxi
            class1=stats.mode(label)[0][0]
            print("%s\t%s" % (current_key,class1))
        total=[]
        total.append(0)
        total.append(1)
        total[0]=[]
        total[1]=[]
        total[0]=total[0]+at[0]
        total[1]=total[1]+at[1]
        current_key = key

