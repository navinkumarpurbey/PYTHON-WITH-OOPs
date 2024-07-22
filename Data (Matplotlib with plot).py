#!/usr/bin/env python
# coding: utf-8

# # MATPLOTLIB

# In[15]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


import numpy as np


# In[3]:


#Simple Exercise

a = np.arange(0, 10)
b = np.arange(11, 21)


# In[4]:


x = np.arange(40, 50)
y = np.arange(60, 70)


# In[5]:


#Plotting using MATPLOTLIB
#plt scatter

plt.scatter(x, y, c = 'g')
#plt.show()

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph In 2D')

plt.savefig('Test.png')


# In[35]:


plt.plot(x, y,'r*', linestyle = 'dashed', linewidth = 2, markersize = 10)
plt.xlabel('some numbers')
plt.title('2D Diagram')


# In[45]:


#subplot

plt.subplot(2,2,1)
plt.plot(x,y,'r-')
plt.subplot(2, 2, 2)
plt.plot(x, y, 'g-*')
plt.subplot(2, 2, 3)
plt.plot(x, y, 'y')
plt.subplot(2, 2, 4)
plt.plot(x, y, 'bo')


# In[46]:


x = np.arange(1, 11)
y = 3 * x + 5


# In[ ]:




plt.scatter(x, y)
plt.plot(x, y)
plt.title("Matplotlib Demo")
plt.xlabel("x-axis caption")
plt.ylabel("y-axis caption")
# In[114]:


#Plotting with keyword Strings

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c = 'c', s = 'd', data = data)
plt.xlabel("entry a")
plt.ylabel("entry b")


# In[52]:


np.pi


# In[54]:


x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)


# In[57]:


#Plot the sin wave using Matplotlib
plt.plot(x, y)
plt.title("Sin Wave form")


# In[64]:


x = np.arange(0, 5 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)


# In[71]:


#Make the first plot
plt.subplot(2, 1, 1)
plt.plot(x, y_sin, 'r--')
plt.title('Sin')

#Make the Second figure
plt.subplot(2, 1, 2)
plt.plot(x, y_cos, 'g^')
plt.title('Cos')


# In[79]:


#Bar Plot

a = [1, 3, 5, 8]
b = [12, 35, 12, 6]

x = [2, 4, 10, 15]
y = [3, 6, 9, 17]

plt.bar(a, b, color = 'r')
plt.bar(x, y, color = 'g')
plt.title("Bar plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")


# In[86]:


#Histogram

x = np.array([2, 4, 10, 15, 24, 56, 75, 23, 45, 56, 89, 90])

plt.hist(x, bins = 10)
plt.title("Histogram")
plt.xlabel("x-axis")
plt.ylabel("y-axis")


# In[101]:


#Box Plot

data = [np.random.normal (0, std, 100)
    for std in range(1, 4)]

plt.boxplot(data, vert = True, patch_artist = True);


# In[95]:


type(data)


# In[109]:


#Pie chart

labels = "C", "C++", "Python", "Java", "MySQL"
sizes = [215, 200, 196, 170, 300]
colors = ["Gold", "Yellow", "Green", "lightcoral", "lightskyblue"]
explode = (0.3, 0, 0, 0, 0)   #explode the first slide with 0.3

plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = "%1.1f%%", shadow = True)
plt.axis('equal')


# In[ ]:




