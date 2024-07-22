#!/usr/bin/env python
# coding: utf-8

# # map() FUNCTION

# In[1]:


def even_odd_number(num):
    if num%2 == 0:
        return "The number {} is even".format(num)
    else:
        return "The number {} is odd". format(num)


# In[4]:


even_odd_number(99)


# In[5]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 24, 56, 89]


# In[6]:


#Map function is the best way to excuted for all details about even and odd numbers
list(map(even_odd_number, lst))


# In[ ]:




