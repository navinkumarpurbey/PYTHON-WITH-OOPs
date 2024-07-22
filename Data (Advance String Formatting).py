#!/usr/bin/env python
# coding: utf-8

# # ADVANCE STRING FORMATTING

# In[1]:


print("Hello Everyone")


# In[2]:


def name_details(name):
    return "The name is {}".format(name)


# In[3]:


name_details("Ganesh")


# In[12]:


def Personal_Details(name, age):
    return "The name is {name} and age is {age}".format(name = name, age = age)


# In[13]:


Personal_Details("Hari", 26)


# In[19]:


def Personal_Details(name, age):
    return "The name is {} and age is {}".format(age, name)


# In[21]:


Personal_Details("Mohan", 34)


# In[ ]:




