#!/usr/bin/env python
# coding: utf-8

# # EDA ON FOOTBALL DATA

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


fifa = pd.read_csv('players_20.csv')


# In[3]:


fifa.head()


# In[5]:


# Using the for loop to check how many names in the title:-
for col in fifa.columns:
    print(col)


# In[7]:


fifa.shape


# In[8]:


fifa['nationality'].value_counts()


# In[10]:


fifa['nationality'].value_counts()[0:10]


# In[11]:


fifa['nationality'].value_counts()[0:10].keys()


# In[13]:


# Plot the BAR Graph
plt.figure(figsize = (8, 8))
plt.bar(list(fifa['nationality'].value_counts()[0:10].keys()), list(fifa['nationality'].value_counts()[0:10]), color = "g")
plt.show()


# In[15]:


Player_Salary = fifa[['short_name', 'wage_eur']]


# In[16]:


Player_Salary.head()


# In[22]:


Player_Salary = Player_Salary.sort_values(by = ['wage_eur'], ascending = False)


# In[23]:


Player_Salary.head()


# In[28]:


plt.figure(figsize = (8, 8))
plt.bar(list(Player_Salary['short_name'])[0:5], list(Player_Salary['wage_eur'])[0:5], color = ["Red", "Yellow", "Orange", "purple", "Green"])
plt.xlabel('Players name')
plt.show()


# In[29]:


fifa['nationality'] == 'Germany'


# In[34]:


Germany = fifa[fifa['nationality'] == 'Germany']


# In[35]:


Germany.head(10)


# In[38]:


Germany.sort_values(by = ['height_cm'], ascending = False).head()


# In[39]:


Germany.sort_values(by = ['weight_kg'], ascending = False).head()


# In[40]:


Germany.sort_values(by = ['wage_eur'], ascending = False).head()


# In[42]:


Germany[['short_name', 'wage_eur']].sort_values(by = ['wage_eur'], ascending = False).head()


# In[43]:


# Shooting
Player_Shooting = fifa[['short_name', 'shooting']]


# In[44]:


Player_Shooting.head()


# In[45]:


Player_Shooting.sort_values(by = ['shooting'], ascending = False).head()


# In[46]:


# Defending
Player_Defending = fifa[['short_name', 'defending', 'nationality', 'club']]


# In[47]:


Player_Defending.head()


# In[48]:


Player_Defending.sort_values(by = ['defending'], ascending = False).head()


# In[49]:


real_madrid = fifa[fifa['club'] == 'Real Madrid']


# In[50]:


real_madrid.head()


# In[51]:


real_madrid.sort_values(by = ['wage_eur'], ascending = False).head()


# In[53]:


real_madrid.sort_values(by = ['shooting'], ascending = False).head()


# In[54]:


real_madrid.sort_values(by = ['defending'], ascending = False).head()


# In[55]:


real_madrid['nationality'].value_counts()


# In[ ]:





# In[ ]:




