#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# Five functions of strings in python.

# In[1]:


name = "Aman Singh"


# In[2]:


name.isalpha() # done during class


# In[3]:


name.index("S") # done during class


# In[8]:


name.find("n") # Function Find. 1


# In[10]:


name.count("Aman") # Function Count. 2


# In[11]:


name.isalnum() # function is alphanumeric. 3


# In[17]:


email = "aman280895" # Function is alphanumeric. 3


# In[18]:


email.isalnum()


# In[20]:


email.isnumeric() # function is numeric. 4


# In[23]:


new_email = email.replace("aman280895", "Aman334") # function repalce. 5


# In[24]:


new_email


# # Assignment 2 
# Five Functions of list

# In[34]:


lst = [4,5,9,6, "Letsupgade", 65.25]


# In[35]:


lst.append("trip")


# In[36]:


lst # during class


# In[37]:


lst.insert(2,"I am learning")


# In[38]:


lst # during class


# In[43]:


numbers = [25, 29,256,758,569]


# In[46]:


numbers.sort()


# In[48]:


numbers # function sort. 1


# In[49]:


lst.pop() # function pop - removes and returns the last function of the list


# In[51]:


lst # 2


# In[52]:


new_lst = lst.copy() # Function copy .3


# In[53]:


new_lst


# In[55]:


numbers.index(29) # function index. 4


# In[56]:


lst.clear() # Function Clear. 5


# In[57]:


lst


# # Assignment 3
# Five default function of dictionaries.

# In[58]:


dit = {"key" : "value", "India" : "Delhi", "USA" : "Washington DC", "Brazil" : "Rio" }


# In[60]:


dit.get("India") # during class


# In[61]:


dit.items() # function items. 1 


# In[62]:


del[dit["USA"]] 


# In[63]:


dit


# In[72]:


dit1 = {"Austria" : " Vienna"}


# In[73]:


dit.update(dit1) # function Update. 2


# In[74]:


dit 


# In[76]:


dit_cap = dit.copy() # Function copy. 3


# In[77]:


dit_cap


# In[84]:


key = { "India", "Austria", "USA", "Pakistan", "Czech Republic"}
value  = "Country"


# In[87]:


countries = dict.fromkeys(key, value) # function fromkeys . 4 


# In[88]:


countries


# In[89]:


countries.popitem() # function popitem. 5


# In[91]:


countries.clear()


# In[92]:


countries


# In[ ]:




