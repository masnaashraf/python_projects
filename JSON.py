#!/usr/bin/env python
# coding: utf-8

# In[19]:


dict_d={}
dict_d['tom']={
                'name':'Tom',
                'address':'blue street,ny',
                'phone':98989898
}

dict_d['john']={
                'name':'john',
                'address':'capital street,ny',
                'phone':23232323
}

#converting into json format
import json
js=json.dumps(dict_d)
print(js)
print("typeof this item is :",type(js))


# In[13]:


#converting it into a file
with open("C:/Users/Masna_2/Desktop/python/data analytics/book.txt","w") as f:
    f.write(js)


# In[18]:


#reading the written file
f=open("C:/Users/Masna_2/Desktop/python/data analytics/book.txt","r")
file_read=f.read()
print(file_read)


# In[21]:


jk=json.loads(js)
print(jk)
print("the type of this is :",type(jk))


# In[24]:


print(dict_d['tom'])


# In[25]:


#getting the value of a single item 
print(dict_d['tom']['address'])


# In[27]:


#printing the records one by one
for person in dict_d:
    print(dict_d[person])
    


# In[ ]:




