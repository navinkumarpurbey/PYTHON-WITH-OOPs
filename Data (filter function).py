#!/usr/bin/env python
# coding: utf-8

# # FILTER FUNCTION

# In[1]:


def even(num):
    if num%2 == 0:
        return True


# In[3]:


even(4)


# In[6]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]


# In[7]:


list(filter(even, lst))


# In[9]:


#Using the lambda function
list(filter(lambda i : i%2 == 0, lst))


# In[ ]:




