#!/usr/bin/env python
# coding: utf-8

# # LIST COMPREHENSION

# In[1]:


lst1 = []

def list_square(lst):
    for i in lst:
        lst1.append(i * i)
        
    return lst1


# In[2]:


list_square([1, 2, 3, 4,5])


# In[3]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[10]:


#using the List Comprehension
lst1 = [i * i for i in lst if i%2!=0]


# In[11]:


print(lst1)


# In[ ]:




