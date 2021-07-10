#!/usr/bin/env python
# coding: utf-8

# In[1]:


#type() used to find type of datatype
a=5;b="ml"
print(a,"is of type",type(a))
print(b,"is a type of ",type(b))


# In[3]:


#isinstance() function to the datatype belongs to particular class or not
a=1+2j
print(a,"the type of a is ",type(a))
print(isinstance(1+3j,complex))


# In[4]:


b=9
print(isinstance(b,string))


# In[7]:


b=9
print(isinstance(b,str))
print(isinstance(1,int))


# In[6]:


c='k'
print(isinstance(c,str))


# In[ ]:




