#!/usr/bin/env python
# coding: utf-8

# # NUMPY

# In[1]:


import numpy as np


# In[3]:


#create numpy array

arr1=np.array([])


# In[4]:


type(arr1)


# In[5]:


#create 1-D array

arr1d=np.array([0,1,2,3])
arr1d


# In[6]:


#create 2-d array

arr2d=np.array([[1,2,3],[4,5,6]])
arr2d


# In[8]:


#ndmin

arrndim=np.array([],ndmin=4)


# In[9]:


arrndim


# In[12]:


#dtype
arrdtype=np.array([],dtype=float, ndmin=3)
arrdtype


# In[13]:


# #supported data types
# bool_
# int_
# int8
# int6
# int32
#uint32
#float16



# In[20]:


#3-d array
arr3d=np.array([[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]])
arr3d


# In[15]:


#0-d array
z=np.array(12)
z


# In[21]:


#to check the dimension

arr3d.ndim


# In[18]:


arr2d.ndim


# In[23]:


#array Indexing
   
a1=np.array([9,8,7,6,5,4,3,2,1])
a1[3]


# In[24]:


arr2d[1,2]


# In[25]:


a3d=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
a3d


# In[26]:


a3d[0,1,2]


# In[27]:


a3d[-1,-2,-1]


# In[33]:


a3d[0]


# In[30]:


a3d[-1,-2]


# In[31]:


a3d[-1,-2,-1]


# In[35]:


#slicing
#[start:end]
#[start:end:step]

a3d[-1, 0:3]


# In[37]:


a3d[0,0,1:2]


# In[38]:


a3=np.array([[3,4,5],[6,7,8],[1,2,3],[9,1,10]])
a3


# In[40]:


a3[-2, 1:3]


# In[42]:


# #np data types
# i - integer
# b - boolean
# u - unsigned int
# f - float
# c - complex float
# m - timedelta
# M - datatime
# O - object
# S - string
# U - unicode string
# V - void (memory fix chunk)


# In[44]:


b1=np.array([1,2,3,4,5], dtype='i')
b1.dtype


# In[49]:


b3= np.array(["arm", "shyam", "haribam"], dtype="S")
b3.dtype


# In[51]:


#astype
b3.astype("U")


# # copy and view
# 
# #Assignment-2
# 
# Deep copy vs Swallo copy in python
# 
# copy vs view in numpy

# In[52]:


#copy and View 

b3


# In[54]:


c3=b3.copy()
c3


# In[55]:


#view

d3=b3.view()


# In[56]:


#difference between view and array

arr1=np.array([2,3,4,5,6,7])


# In[57]:


arr2=arr1.copy()
arr3=arr1.view()


# In[58]:


arr2


# In[59]:


arr3


# In[60]:


#shape
arr3.shape


# In[61]:


arr3d.shape


# In[62]:


arr2d.shape


# In[63]:


nj=np.array([],ndmin=5)


# In[64]:


nj.shape


# In[65]:


#reshaping
a1


# In[66]:


a1.reshape(3,3)


# In[67]:


aa=np.array([9, 8, 7, 6, 5, 4, 3])
aa.shape


# In[68]:


a1=np.array([9, 8, 7, 6, 5, 4, 3, 2, 1,4,5,6])
a1.shape


# In[69]:


a1.reshape(2,6)


# In[70]:


a1.reshape(12,1)


# In[71]:


a1.reshape(2,3,2)


# In[72]:


#reshape into unknown dimension

a1


# In[73]:


a1.reshape(2,1,-1)


# In[74]:


a1.reshape(3,-1)


# In[75]:


#iterating in array

for i in arr1:
    print(i)


# In[81]:


arr3d


# In[77]:


for i in arr2d:
    print(i)
    


# In[78]:


for i in arr2d:
    for j in i:
        print(j)


# In[84]:


for i in a3d:
    for j in i:
        for k in j:
            print(k)


# In[80]:


#nditer
for i in np.nditer(arr3d):
    print(i)


# In[89]:


aa3=np.array([[3,4,5],[6,7,8],[1,2,3]])
aa3


# In[92]:


for i in aa3:
    for j in i:
        for k in j:
            print(k)


# In[91]:


#ndenumerate

for index, value in np.ndenumerate(arr3d):
    print(index, ':', value)


# In[95]:


#concatenate

a1=np.array([[2,3,4],[22,33,44]])
a2=np.array([[5,6,7],[44,66,77]])
newarr=np.concatenate((a1,a2))
newarr


# In[104]:


#axis =1
n2=np.concatenate((a1,a2), axis=1)


# In[105]:


a1


# In[106]:


a2


# In[107]:


n2


# In[ ]:





# In[10]:


#hstack
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
np.hstack((arr1,arr2))


# In[2]:


#vstack


# In[11]:


#stack
np.dstack((arr1,arr2))


# In[12]:


arr2d


# In[13]:


#searching in array
import numpy as np
arr2d=np.array([[1,2,3],[4,5,6]])
arr2d


# In[14]:


np.where(arr2d==2)


# In[15]:


#search sorted

arr1=np.array([1,3,5,9,11])
x=np.searchsorted(arr1,7)


# In[16]:


x


# In[18]:


arr1=np.array([15,12,1,3,5,9,11])
x=np.searchsorted(arr1,8, side="left")
x


# In[19]:


arr2d=np.array([[9,33,4],[44,5,3]])
arr2d


# In[20]:


np.sort(arr2d)


# In[21]:


#random

from numpy import random
x=random.rand(4)
x


# In[22]:


x=random.randint(4)
x


# In[24]:


x=random.randint(41, size=5)
x


# In[25]:


x=random.randint(41, size=(5,3))
x


# In[26]:


y=random.choice([2,4,6,8], size=(3,3))
y


# In[ ]:




