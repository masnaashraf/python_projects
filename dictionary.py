#!/usr/bin/env python
# coding: utf-8

# In[1]:


#empty dictionary
d1=dict()
print(type(d1))


# In[2]:


#dictionary with integer key
d2={1:"abc",2:"efg"}
print(d2)


# In[4]:


#dictionary with mixed keys
d3={'name':'satish',1:['abc',1]}
print(type(d3))


# In[5]:


#we cannot include mutable datatype list list into key
d4={'name':'satish',[1,2,3]:3}
print(type(d4))


# In[9]:


#creating dictionary with list of tuples and dict keyword
d5=dict([(1,'satish'),(2,"ram"),('day',"wednesady")])
print(d5)
print(type(d5))


# In[12]:


#accesing values from dictionary
d6={1:'a',2:'b',3:'c','fgh':4}
print(d6[1])
print(d6['fgh'])
print(d6['a'])


# In[17]:


"""accesing values from dictionary using dictname.get() method . and if the key is not present it gives 
"None" instead of error msg"""
d6={1:'a',2:'b',3:'c','fgh':4}
print(d6.get(1))
print(d6.get('fgh'))
print(d6.get('a'))


# In[19]:


#add elements to dictionary
d7={1:100,2:200}
d7[3]=300
d7['four']=400
print(d7)


# In[ ]:


#modify elemnt of dictionary


# In[20]:


#modify elements of dictionary
d7={1:100,2:200}
d7[2]='two'
print(d7)


# In[ ]:





# In[21]:


#adding elements of dictionary
d7={1:100,2:200}
d7[3]='two'
print(d7)


# In[29]:


#to remove particular element from dictionary
d7={1:100,2:200,3:300}
print(d7.pop(2))
print(d7)


# In[26]:


#removes artibaty item
d8={1:'a',2:'b',3:'c',4:'e'}
print(d8.popitem())
print(d8)


# In[31]:


#deleting a particular element dictionar "del"
del d8[3]
print(d8)


# In[33]:


#removing all items in dictionary "clear"
d8.clear()
print(d8)


# #removing entire dictionary
# d9={'a':1,'b':2,"c":3}
# del d9
# print(d9)
# #name error as the dictionary is deleted using del keyword

# In[35]:


#copy dictionary using copy()
d9={'a':1,'b':2,"c":3}
d10=d9.copy()
print(d10)


# In[36]:


#fromkeys returns dictionary with specified value and key
x=('a','b','c')
y=0
d11=dict.fromkeys(x,y)
print(d11)


# In[36]:


#fromkeys returns dictionary with specified value and key
x=('a','b','c')
y=0
d11=dict.fromkeys(x,y)
print(d11)


# In[39]:


#fromkeys returns dictionary with specified value and key
x=('a','b','c')
y=1,2
d13={}.fromkeys(x,y)
print(d13)


# In[40]:


d14=dict.fromkeys(('a','e','i'),0)
print(d14)


# In[42]:


d14=dict.fromkeys(['a','e','i'],1)
print(d14)


# In[43]:


d15={1:10,2:20,3:30,4:30}
print(d15.items())


# In[ ]:





# In[44]:


d15={1:10,2:20,3:30,4:30}
print(d15.values())


# In[45]:


d15={1:10,2:20,3:30,4:30}
print(d15.keys())


# In[45]:


d15={1:10,2:20,3:30,4:30}
print(d15.keys())


# In[48]:


d15={1:10,2:20,3:30,4:30}
for i in d15.items():
    print(i)


# In[49]:


d15={1:10,2:20,3:30,4:30}
for i in d15.values():
    print(i)


# In[46]:


#to get all available methods and attributes of dictionary
d={}
print(dir(d))


# In[51]:


#using comprehension to create dictionary
d13={'a':1,'b':2,'c':3,'d':4}
d14={k:v for k,v in d13.items() if v>2}
print(d14)


# In[52]:


#using comprehension to create dictionary
d13={'a':1,'b':2,'c':3,'d':4}
d14={k+'c':v*2 for k,v in d13.items() if v>2}
print(d14)


# In[56]:


#using comprehension to create dictionary
d13={'a':1,'b':2,'c':3,'d':4}
d14={k:v**2*3 for k,v in d13.items() if v>2}
print(d14)


# In[ ]:


"""entering marks of students and calculating average(here number of subjects may varry per student)"""
def getDataFromStudent():
    d={}
    while True:
        student_id=input("Enter the student id:")
        student_marks=input("Enter student marks with comma seperated list:")
        more_student=input("enter 'no' if there is no more students details to enter: ")
        if student_id in d:
            print("this student detail is already entered")
        else:
            d[student_id]=student_marks.split(",")
        if more_student.lower()=="no":
            return d

student_dict=getDataFromStudent()
print(student_dict)


# 

# In[ ]:




