#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


# Playing with DataFrame

df = pd.DataFrame(np.arange(0,16).reshape(4,4), index = ['Row1', 'Row2', 'Row3', 'Row4'], 
                  columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4'])


# In[5]:


df.head()


# In[6]:


# Checking the total values using Threshold

np.set_printoptions(threshold=np.inf)  # Show all elements
arr = np.arange(0, 28).reshape(7, 4)
print(arr)


# In[7]:


arr = np.arange(0, 28).reshape(7, 4)
print(arr.shape)  # This will output (7, 4) confirming the shape


# In[8]:


arr = np.arange(0, 28).reshape(7, 4)
print(arr.all())  # This will check if all elements are True (valid)


# In[9]:


# CSV files from above Data
df.to_csv('Test1.csv')


# In[10]:


#Accessing the Elements
#using loc

df.loc['Row2']
type(df.loc['Row2'])


# In[11]:


#Another Accessing the another Elements is iloc

df.iloc[2:3 , 2:3]
type(df.iloc[2:3 , 2:3])


# In[12]:


#converting Dataframe into array

df.iloc[:,1:].values


# In[13]:


df


# In[14]:


#Checking the data is null or not null
df.isnull().sum


# In[15]:


#Checking the unique values in column1

df['Column 2'].value_counts()


# In[16]:


#We can also retrive the data from the table

df[['Column 1', 'Column 3', 'Column 4']]


# In[17]:


df.info


# In[18]:


df.describe()


# In[19]:


df = pd.read_csv('Test1.csv')


# In[20]:


df.head()


# In[21]:


test_df = pd.read_csv('Test1.csv', sep = ';')


# In[22]:


test_df.head()


# # CSV

# In[23]:


from io import StringIO, BytesIO


# In[25]:


df.dtypes


# In[31]:


data = 'a, b\n "hello,\\BOB\\, nice to see you", 5'


# In[32]:


pd.read_csv(StringIO(data), escapechar = '\\')


# # READ JSON TO CSV

# In[4]:


Data = '{"Employee_name" : "Ram", "Manager_name" : "Dashrath", "Job Profile" : [{"title1" : "team_leader", "title2" : "HR"}] }'
pd.read_json(Data)


# In[ ]:





# In[ ]:




