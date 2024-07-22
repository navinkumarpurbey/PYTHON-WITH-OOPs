#!/usr/bin/env python
# coding: utf-8

# # EDA ON IPL DATA 

# In[86]:


# Loading the required libraries:-
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# In[20]:


ipl = pd.read_csv('matches.csv')


# In[21]:


ipl.head()


# In[22]:


#Rows nd Column in the datasets
ipl.shape


# In[23]:


# Here is checking the much numbers value/name of players of the matches
ipl['player_of_match'].value_counts()


# In[24]:


# Getting top 10 players Most man of the match in the ipl
ipl['player_of_match'].value_counts()[0:10]


# In[25]:


# # Getting top 10 players Most man of the match in the ipl
ipl['player_of_match'].value_counts()[0:5]


# In[26]:


# Here using the keys() method for only gets a value name:-
list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[31]:


# Show in Bar grap of top 5 players of the matches:-
plt.figure(figsize = (8, 6))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), list(ipl['player_of_match'].value_counts()[0:5]), color = "g")
plt.show()


# In[32]:


# Getting the frequency of the result column:-
ipl['result'].value_counts()


# In[34]:


ipl['toss_winner'].value_counts()


# In[36]:


# Extracting the records where a team won batting first:- 
Batting_First = ipl[ipl['win_by_runs']!=0]


# In[37]:


Batting_First.head()


# In[43]:


# Making a Histogram:-
plt.figure(figsize = (7, 7))
plt.hist(Batting_First['win_by_runs'])
plt.title("Distubation of Run")
plt.xlabel("Runs")
plt.show()


# In[39]:


Batting_First['win_by_runs'].value_counts()


# In[47]:


# Making the bar-plot for top3 teams who win the matches after batting first:
plt.figure(figsize = (7,7))
plt.bar(list(Batting_First['winner'].value_counts()[0:3].keys()), list(Batting_First['winner'].value_counts()[0:3]), color = ["Blue", "Red", "Yellow"])
plt.xlabel("Team names")
plt.show()


# In[54]:


# Making a PIE chart:-
plt.figure(figsize = (8, 8))
plt.pie(list(Batting_First['winner'].value_counts()), labels = list(Batting_First['winner'].value_counts().keys()), autopct = '%0.1f%%')
plt.show()


# In[63]:


# Extracting those who wins in batting seconds:-
Batting_Second = ipl[ipl['win_by_wickets']!=0]


# In[65]:


Batting_Second.head()


# In[72]:


# making a Histogram:-
plt.figure(figsize = (7,7))
plt.hist(Batting_Second['win_by_wickets'], bins = 20)
plt.xlabel("Wickets")
plt.show()


# In[71]:


Batting_Second['win_by_wickets'].value_counts()


# In[73]:


Batting_Second['winner'].value_counts()


# In[75]:


# Making the bar-plot for Batting Seconds:-
plt.figure(figsize = (8,8))
plt.bar(list(Batting_Second['winner'].value_counts()[0:3].keys()), list(Batting_Second['winner'].value_counts()[0:3]), color = ["purple", "blue", "red"])
plt.show()


# In[82]:


# Making a PIE chart:-
plt.figure(figsize = (8,8))
plt.pie(list(Batting_Second['winner'].value_counts()), labels = list(Batting_Second['winner'].value_counts().keys()),  autopct = "%0.1f%%")
plt.show()


# In[83]:


Batting_Second['winner'].value_counts()


# In[84]:


# Looking at the match played in each season:-
ipl['season'].value_counts()


# In[85]:


# Looking the matched played in each city:-
ipl['city'].value_counts()


# In[87]:


# Finding the how many times team won the match after the wining the toss:-
np.sum(ipl['toss_winner'] == ipl['winner'])


# In[88]:


deliveries = pd.read_csv('deliveries.csv')
#No such csv files so there is error:-


# In[ ]:




