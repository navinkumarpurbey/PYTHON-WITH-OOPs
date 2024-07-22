#!/usr/bin/env python
# coding: utf-8

# # OOPS Tutorial

# In[1]:


# Creating the class name is car:

class Car:
    def __init__(self, window, enginetype, wheels):
        self.windows = window
        self.enginetypes = enginetype
        self.wheels = wheels


# In[3]:


# There is the define about car1 = Car (All the Car items intilize with car1)
car1 = Car(4, "Petrol", 4)


# In[4]:


print(car1)


# In[5]:


print(Car)


# In[7]:


# Excuted the enginetypes
print(car1.enginetypes)


# In[8]:


print(car1.wheels)


# In[19]:


# Creating the class name is car:and define two function inside same class

class Car:
    def __init__(self, window, enginetype, wheels):
        self.windows = window
        self.enginetypes = enginetype
        self.wheels = wheels
        
    def self_driving(self):
        return "The self-driving car is {}".format(self.enginetypes)


# In[20]:


car2 = Car(4, "Disels", 4)


# In[24]:


car2.self_driving()


# In[31]:


# Create a another class name id Person:

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def __str__(self):
        return f"{self.name} ({self.age}) {self.address}"


# In[32]:


p1 = Person("Ram", 20, "Aayodhya")


# In[33]:


print(p1)


# In[36]:


# Examples 
class PersonDetails:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def perDetails(self):
        return "The name is {} and address is {}".format(self.name, self.address)


# In[37]:


p1 = PersonDetails("Laxman", "Ram Mandir")


# In[38]:


p1.perDetails()


# In[ ]:




