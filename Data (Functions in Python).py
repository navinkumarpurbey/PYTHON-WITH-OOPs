#!/usr/bin/env python
# coding: utf-8

# # PYTHON FUNCTION

# In[1]:


#Define function
def my_Function():
    print("Hello I am Back")


# In[2]:


#Calling Function with function name
my_Function()


# In[3]:


num = 24


# In[4]:


#Passing parameter num in function name
def even_odd(num):
    if num%2 == 0:
        print("This is even number")
    else:
        print("This is odd number")


# In[10]:


#Calling the function
even_odd(100)


# In[11]:


#Using return method
def hello_world():
    return "Hello world"


# In[16]:


val = hello_world()


# In[17]:


print(val)


# In[19]:


#Another examples of return method
num1 = 1
num2 = 2


# In[20]:


def sum_numbers(num1, num2):
    return num1 + num2


# In[30]:


val = sum_numbers(20, 80)


# In[31]:


print(val)


# In[36]:


#Or if i not define parameter then 
def sum_number(num3, num4):
    return num3 + num4


# In[38]:


val = sum_number(30, 40)


# In[39]:


print(val)


# In[47]:


#Positional Arguments and Keywords Argument
def student_name(name, Age = 20):
    print("My name is {} and Age is {}. ".format(name, Age))


# In[48]:


student_name("Bhanu")


# In[49]:


#Using *args and **kwargs
def hello(*args, **kwargs):
    print(args)
    print(kwargs)


# In[50]:


hello("Navin", "Rohit", "Virat", age = 20, DOB = 2002)


# In[51]:


#let's make a List and Dictionary
list = ['Navin', 'Rohit', 'Virat']
dict_name = {'age': 20, 'DOB': 2002}


# In[54]:


hello(*list, **dict_name)


# In[55]:


#Defining the parameter lists
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[61]:


def even_odd_Numbers(lists):
    even_sum = 0
    odd_sum = 0
    for i in lists:
        if i%2 == 0:
            even_sum = even_sum + i
            
        else:
            odd_sum = odd_sum + i
    
    return even_sum, odd_sum


# In[62]:


even_odd_Numbers(lists)


# In[3]:


#Using the pass statement
def pass_statement():
    pass


# In[4]:


def my_function():
  print("Hello from a function")


# In[6]:


my_function()


# In[ ]:




