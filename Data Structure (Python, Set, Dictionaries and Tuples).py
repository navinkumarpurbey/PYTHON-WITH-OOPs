#!/usr/bin/env python
# coding: utf-8

# # Sets

# In[6]:


#Defining an empty sets

set_var = set()
print(set_var)
type(set_var)


# In[10]:


#Set never repet duplicate values (to see given examples)

set_values = {1, 2, 3, 4, 5, 3}
set_values
print(set_values)


# In[19]:


set_vari = {"Avengers", "Captian America", "Iron Man", "Natasha Romanoff"}
print(set_vari)
type(set_vari)


# In[22]:


#Inbuilt function in sets

set_vari.add("Hulk")
set_vari


# In[55]:


#Some calculation 

set1 = {"The Avengers", "Age Of Ultron", "Avengers EndGame",}
set2 = {"The Avengers", "Age Of Ultron", "Avengers EndGame", "The Incredible Hulk", "Thor Ragnarok"}
print(set1)


# In[29]:


#Differences in sets

set2.difference(set1)


# In[40]:


#Intersection oin sets

set2.intersection(set1)
set2.intersection_update(set1)

set2


# In[63]:


#Some built in function in sets
# in this built in function .remove() raise error but when error is raise using the .remove() built in function then using .discard()

# using .discard() function
set1.discard("The Avengers")
print(set1)

#using .union() function
set3 = set2.union(set1)
print(set3)


# # Dictionaries

# In[68]:


dict = {}
print(dict)
type(dict)


# In[72]:


dict_examples = {1, 2, 3, 4, 5}
print(dict_examples)
type(dict_examples)


# In[76]:


#So dictonaries have key values

dict_examples2 = {
    "Car" : "Audi",
    "Bike" : "Java",
    "Fruites" : "Banana",
    "Books" : "Atomic habits"}
print(dict_examples2)
type(dict_examples2)


# In[78]:


# Loops in dictonaries keys

for x in dict_examples2:
    print(x)


# In[85]:


#Loops in Dictonaries only values

for x in dict_examples2.values():
    print(x)


# In[86]:


#Loops in dictonaries Values in term of items

for x in dict_examples2.items():
    print(x)


# In[89]:


# Adding items in the dictionaries

dict_examples2["car2"] = "Lamborghini"
dict_examples2


# In[93]:


dict_examples2["car3"] = "Ferrari"
dict_examples2


# In[104]:


dict_examples2["Car"] = "BMW"
dict_examples2


# In[112]:


# delete the key from dictonaries

del dict_examples2["Bike"]
print(dict_examples2)


# # Nested Dictonaries

# In[117]:


car1_model = {"Maruti Swift" : "5.99 - 9.03 Lakhs"}
car2_model = {"Hyundai Creta" : "11 - 20.15 Lakhs"}
car3_model = {"Toyata Fortuner" : "33.43 - 51.44 Lakhs"}
car4_model = {"Mahindra Thar" : "11.25 - 17.20 Lakhs"}

car_type = {"car1":car1_model, "car2":car2_model, "car3":car3_model, "car4":car4_model}


# In[119]:


print(car_type)


# In[121]:


print(car_type["car1"]["Maruti Swift"])


# # Tuples

# In[125]:


my_tuple = tuple()
print(my_tuple)


# In[127]:


type(my_tuple)


# In[131]:


my_tuple2 = ("Apple", "Banana", "Cherry", "Pomogranet")
print(my_tuple2)


# In[133]:


type(my_tuple2)


# In[149]:


my_tuple2 = ("Hello", "World", "Buddy", "World")
print(my_tuple2)


# In[137]:


#Tuple remove all the items not a single items
my_tuple2


# In[146]:


print(type(my_tuple2))
print(my_tuple2)


# In[148]:


#Inbuilt function

my_tuple2.index("Hello")


# In[150]:


my_tuple2.count("World")

