#!/usr/bin/env python
# coding: utf-8

# # LAMBDA FUNCTION

# In[1]:


#This is how Lambda function writen
addition = lambda a, b : a + b


# In[2]:


addition(12, 7)


# In[3]:


#If there is condition then,
even = lambda a: a%2 == 0


# In[4]:


even(23)


# In[6]:


#This is the function and we can see the (Lambda function is looking cool in front of Function)
def even1(num):
    if num%2 == 0:
        return True
    else:
        return False


# In[7]:


even1(24)


# In[8]:


#We add the 3 number 
add = lambda a, b, c : a + b + c


# In[10]:


add(1, 2, 3)


# In[12]:


#Using the function and lambda function for make number double
def num_double(n):
    return lambda a : a * n

MyDoubler = num_double(2)


# In[14]:


print(MyDoubler(12))


# In[15]:


#Using the function and lambda function for make number double, tripler
def nums(n):
    return lambda a : a * n

MyDoubler = nums(2)
Mytripler = nums(3)


# In[16]:


print(MyDoubler(13))


# In[17]:


print(Mytripler(13))


# In[ ]:




