#!/usr/bin/env python
# coding: utf-8

# # EXCEPTION HANDLING

# In[3]:


a = 1
b = 'd'
c = a + b


# In[12]:


try:
    a = 1
    b = 'd'
    c = a + b
except TypeError:
    print("This is the Type error and write carefully")

except Exception as ex:
    print(ex)


# In[6]:


print(x)


# In[10]:


try:
    print(x)
    
except Exception as ex:
    print(ex)


# In[ ]:




