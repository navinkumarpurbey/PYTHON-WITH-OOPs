#!/usr/bin/env python
# coding: utf-8

# # INHERITANCE

# In[18]:


# All the class variable are public
# Car Blueprint
# This is Parent Class of Audi

class Car():
    def __init__(self, windows, door, enginetype):
        self.windows = windows
        self.door = door
        self.enginetype = enginetype
        
    def drive(self):
        print("The Person Drives the Car!")


# In[5]:


car = Car(5, 4, "Petrol")


# In[10]:


car.drive()


# In[13]:


car.enginetype


# In[14]:


car.windows


# In[22]:


# This is child or sub class of Car
# Create another class is:

class Audi(Car):
    def __init__(self, windows, door, enginetype, enableAi):  #If you have extra things then add in this parameter and what have extra functions of audi car
        super().__init__(windows, door, enginetype)
        self.enableAi = enableAi
        
    def selfdrive(self):
        print("The Audi car is selfDriven car so this is easy for Human and one things is that Audi is Hybrid car.")


# In[24]:


# AudiQ7 is a model name i put form of variable
AudiQ7 = Audi(5, 4, "Petrol & Electric", True)


# In[25]:


AudiQ7.selfdrive()


# In[27]:


AudiQ7.drive()


# In[28]:


AudiQ7.enginetype


# In[ ]:


##Examples of Inheritance to check how they works and behaviours:-


# In[8]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


# In[9]:


class Student(Person):
  def __init__(self, fname, lname, graduationyear):
    super().__init__(fname, lname)
    self.graduationyear = graduationyear
    
  def StudentBehaviours(self):
  	print("Mike Olsen is ia good boy carry with good behaviours")


# In[11]:


x = Student("Mike", "Olsen", "Good")
x.firstname


# In[ ]:




