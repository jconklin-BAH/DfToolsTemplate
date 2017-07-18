
# coding: utf-8

# In[12]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy
from scipy import stats


# In[13]:

data_filepath = 'XXXXXXXXXX'


# In[14]:

data = pd.read_csv(data_filepath)


# In[15]:

def findAndReplace(data, column, find, replace):
    index = 0
    for value in data[column]:
        if value == find:
            #print('changing %s at line %d to %s'%(value, index, replace))
            data.set_value(index, column, replace)
        index += 1 


# In[16]:

def convertStringsToInt(data, column):
    index = 0
    for value in data[column]:
        if type(value) == str:
            #print('changing %s %s at line %d to %d %s'%(value, str(type(value)), index, float(value), str(type(float(value)))))
            data.set_value(index, column, int(value))
        index += 1


# In[17]:

def replacePartOfEach(data, column, toReplace, replaceWith):
    index = 0
    for value in data[column]:
        if type(value) == str:
            data.set_value(index, column, value.replace(toReplace, replaceWith))
        index += 1


# In[18]:

def removeFromEach(data, column, toRemove):
    replacePartOfEach(data, column, toRemove, '')


# In[19]:

contractList=[]
#Each item in the list is a Contract object, representing a unique contract from data


class Contract:
    def __init__(self, contractID, indeces, ogAmt, fndAmt, difAmt):
        self.contractNumber = contractID #The unique ID given to each contract in data
        self.listOfIndeces = indeces #list of all the indeces at which individual projects within this contract can be found
        self.originalAmount = ogAmt  #the original dollar amount for this contract
        self.fundedAmount = fndAmt   #the actual dollar amount budgeted for this contract
        self.diffBetweenDollars = difAmt #the difference between the actual amount paid and original budget


contractDict = {}
'''
Each key represents an individual contract.
Each value represents a list containing all of the indeces
    at which an individual project for said contract is stored in the data.
This dictionary is used to help populate contractList
'''

#Organizes data into contractDict with a contract ID for each key and a list of individual projects for each values
index = 0
for num in data['XXXXXXXXXX']:
    if num in contractDict:
        contractDict[num].append(index)
    else:
        contractDict[num] = []
        contractDict[num].append(index)
    index += 1
#Uses contractDict to populate contractList with Contract objects     
for key in contractDict:
    contractList.append(Contract(key, contractDict[key], data['XXXXXXXXXX'][contractDict[key][0]],
                                 data['XXXXXXXXXX'][contractDict[key][0]],
                                 data['XXXXXXXXXX'][contractDict[key][0]]))


# In[22]:

x = range(10)
xLabel = 'XXXXXXXXXX'
y = range(10)
yLabel = 'XXXXXXXXXX'


# In[23]:

stats.pearsonr(x, y)


# In[25]:

plt.scatter(x,y,s=10)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.show()


# In[ ]:



