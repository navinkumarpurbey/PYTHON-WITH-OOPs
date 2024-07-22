#!/usr/bin/env python
# coding: utf-8

# # ITERABLES VS ITERATOR

# In[1]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 46, 56, 90, 100, 400]


# In[2]:


#using the for loop through the iterator
for i in lst:
    print(i)


# In[23]:


list1 = iter(lst)


# In[24]:


list1


# In[31]:


next(list1)


# In[32]:


for j in list1:
    print(j)


# In[61]:


#Even string is iteration the convert into Iterator
strname = ("Banana", "Apple", "cherry")


# In[62]:


name = iter(strname)


# In[66]:


print(next(name))


# In[79]:


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x


# In[95]:


myclass = MyNumbers()
myiter = iter(myclass)


# In[98]:


next(myiter)


# In[96]:


# Using loop for limited number will be printed
for i in range(5):
    print(next(myiter))


# In[ ]:




