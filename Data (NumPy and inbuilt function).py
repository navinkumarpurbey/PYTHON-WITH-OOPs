#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install numpy


# In[5]:





# In[ ]:


conda update -n base -c defaults conda


# In[5]:


import numpy as np


# In[6]:


my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)


# In[16]:


arr


# In[7]:


type(arr)


# In[8]:


arr.shape


# In[46]:


#Multinested Array two dimensional array

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]
my_list3 = [11, 12, 13, 14, 15]
my_list4 = [16, 17, 18, 19, 20]


# In[38]:


arr = np.array([my_list1, my_list2, my_list3, my_list4])


# In[39]:


arr


# In[12]:


type(arr)


# In[14]:


#Check the shape of the array
arr.shape


# In[16]:


arr.reshape(5, 4)


# In[18]:


#array reshaping method
arr.reshape(2, 10)


# # Indexing

# In[145]:


arr = ([1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[146]:


arr = np.array(arr)


# In[147]:


arr


# In[28]:


type(arr)


# In[30]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[34]:


# Taking the indexing position

arr[3]
arr[6]


# In[41]:


arr


# In[43]:


arr[:,:]


# In[47]:


arr[:,3:]


# In[49]:


arr[2:,:]


# In[51]:


arr[0:2,0:2]


# In[60]:


arr[0:3,1:4]


# In[62]:


ex_list1 = [2, 4, 6, 7, 10, 12]
ex_list2 = [4, 6, 8, 11, 13, 14]
ex_list3 = [10, 20, 30, 40, 50, 60]


# In[66]:


arr = np.array([ex_list1, ex_list2, ex_list3])


# In[68]:


print(arr)


# In[70]:


arr


# In[73]:


# Taking the index position row and column

arr[0:3,2:6]


# In[75]:


arr[0:3,0:3]


# In[83]:


arr[1:, 4:]


# In[87]:


arr[1:2,1:4]


# In[90]:


arr[2:3 , 2:5]


# In[103]:


# Built in function in numpy

arr = np.arange(0,10, step = 4)
arr


# In[110]:


np.linspace(1, 10, 40)


# In[121]:


# copy() function and broadcasting

arr[3:] = 100
arr


# In[123]:


arr1 = arr


# In[125]:


arr1[3:] = 500
arr


# In[127]:


arr


# In[129]:


arr1 = arr.copy()


# In[132]:


# showing both previous and after using arr1[3:] = 1000 then,

print(arr1)
arr1[3:] = 1000
print(arr1)


# In[136]:


arr


# In[138]:


arr1


# In[141]:


# Some conditions very useful in Exploratory Data Analysis

value = 2
arr>2


# In[143]:


arr[arr<300]


# In[155]:


# Create array and reshape

np.arange(0,10).reshape(5, 2)


# In[160]:


np.ones(10, dtype = int)


# In[162]:


np.ones(8, dtype = float)


# In[165]:


np.ones((5,2),dtype = float)


# In[167]:


# random distributation

np.random.rand(3,3)


# In[176]:


arr_ex = np.random.rand(4,4)


# In[177]:


arr_ex


# In[169]:


import seaborn as sns
import pandas as pd


# In[182]:


sns.distplot(pd.DataFrame(arr_ex.reshape(16,1)))

