#!/usr/bin/env python
# coding: utf-8

# # Python Data Structure and Boolean

# In[2]:


True


# In[4]:


False


# In[6]:


type(True)


# In[8]:


type(False)


# In[32]:


my_string = "Navin"


# In[26]:


print(my_string.isalnum())


# In[23]:


print(my_string.istitle())


# In[37]:


print(my_string.isalnum())
print(my_string.isalpha())
print(my_string.isdigit())
print(my_string.istitle())
print(my_string.isupper())
print(my_string.islower())
print(my_string.isspace())
print(my_string.endswith('n'))
print(my_string.startswith('N'))


# # BOOLEAN AND LOGICAL OPERATORS

# In[39]:


True and True


# In[41]:


True and False


# In[43]:


True or True


# In[45]:


True or False


# In[57]:


my_example = "12345"
my_string = "Navin"


# In[61]:


my_string.isalpha() or my_example.isnum()


# # Lists

# In[63]:


list


# In[65]:


ls_example = []


# In[67]:


type(ls_example)


# In[69]:


lists = ['mathematics', 340, 560, "chaggebale", 789, "Name"]


# In[71]:


print(lists)


# In[73]:


type(lists)


# In[87]:


len(lists)


# In[90]:


lists[2]


# # Append

# In[80]:


lists.append("Navin")


# In[82]:


lists.append("purbey")


# In[84]:


lists


# In[93]:


#indixing in the list
lists[6]


# In[95]:


lists[3:]


# In[99]:


lists[3:7]


# In[104]:


lists.append(["ere", "siri", "Google Home"])


# In[105]:


lists


# # Inserts

# In[101]:


lists.insert(1, 100)


# In[103]:


lists


# In[ ]:




