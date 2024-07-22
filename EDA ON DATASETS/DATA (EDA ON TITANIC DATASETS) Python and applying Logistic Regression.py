#!/usr/bin/env python
# coding: utf-8

# # EDA WITH TITANIC DATA SET 

# In[102]:


#Import all the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[103]:


train = pd.read_csv("titanic_train.csv")


# In[104]:


train.head()


# In[105]:


#Checking the null value or not
train.isnull()


# In[106]:


#Using the seaborn for the proper visulized the Data
#yticklabels - represent all the labels in y axis data like as 0 to 890 (left side)
#cbar = False - represents the indication like this (1.0, 0.8, 0.6)

sns.heatmap(train.isnull(), yticklabels = False, cmap = 'coolwarm')


# In[107]:


sns.set_style('whitegrid')
sns.countplot(x = 'Survived', data = train, hue = 'Sex')


# In[108]:


sns.set_style("whitegrid")
sns.countplot(x = 'Survived', data = train, hue = 'Pclass')


# In[109]:


sns.distplot(train['Age'].dropna(), kde = False, bins = 60)


# In[110]:


sns.distplot(train['Age'].dropna(), bins = 40)


# In[111]:


sns.countplot(x = "SibSp", data = train)


# # DATA CLEANING

# In[112]:


plt.figure(figsize = (12, 7))
sns.boxplot(x = "Pclass", y = "Age", data = train, palette = "rainbow")


# In[113]:


#This functionf or the isnull value in 'Age'
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        
        if Pclass == 1:
            return 37
        
        elif Pclass == 2:
            return 29
        
        else:
            return 24
        
    else:
        return Age


# In[114]:


#Apply the above function
train["Age"] = train[['Age', 'Pclass']].apply(impute_age, axis = 1)


# In[115]:


sns.heatmap(train.isnull(), yticklabels = False, cmap = "coolwarm")


# In[116]:


train.drop('Cabin', axis = 1, inplace = True)


# In[117]:


sns.heatmap(train.isnull(), data = train, cmap = 'coolwarm')


# In[118]:


train.head()


# In[ ]:





# In[ ]:




