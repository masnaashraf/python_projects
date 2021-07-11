#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys
sys.path.append('C:/Users/Masna_2/Desktop/python/data analytics/MyModule/')


# In[9]:


import my_module


# In[10]:


get_ipython().run_line_magic('pinfo2', 'my_module.addnum')


# In[13]:


c=my_module.addnum(1,2,3,-2)
print(c)


# In[7]:


d=my_module.addAllnumeric(1,2,3)
print(d)


# In[ ]:




