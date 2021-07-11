#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funcMsg(msg):
    print(msg)

funcMsg("hello world")
funcMsg("how r u")


# In[24]:


'''function that prints message if the passed arg is string '''
def funcstr(msg):
    '''this checks for string'''
    if isinstance(msg,str):
        print(msg)
    else:
        '''this deals with non string argument'''
        print("your input argument is not string")
        print("but here is what you have supplied",msg)

funcstr("hello world")
funcstr(1234)


# In[22]:


get_ipython().set_next_input('print funcMsg');get_ipython().run_line_magic('pinfo', 'funcMsg')


# In[ ]:


print funcMsg


# In[ ]:


print funcMsg


# In[12]:


#this gives you the documentation you have written inside the function
get_ipython().set_next_input('print funcstr');get_ipython().run_line_magic('pinfo', 'funcstr')


# In[ ]:


print funcstr


# In[18]:


get_ipython().set_next_input('print funcstr');get_ipython().run_line_magic('pinfo', 'funcstr')


# In[ ]:


print funcstr


# In[26]:


get_ipython().set_next_input('print funcstr');get_ipython().run_line_magic('pinfo', 'funcstr')


# In[ ]:


print funcstr


# In[28]:


#this gives the entire implementation of the function along with the documentation
get_ipython().set_next_input('print funcstr');get_ipython().run_line_magic('pinfo2', 'funcstr')


# In[ ]:


print funcstr


# In[ ]:


print funstr


# In[30]:


#documentation of built in function also can be obtained by this
get_ipython().run_line_magic('pinfo', 'len')


# In[30]:


#details of built in function also can be obtained by this only if the fnction is written in python and not in c
get_ipython().run_line_magic('pinfo', 'len')


# In[31]:


#gives details of the function documentation
help(funcstr)


# In[33]:


def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print(a+b+c)
    else:
        print("enter either integer or float as argument")

checkArgs(20,90,10)


# In[57]:


#to pass arbitary number of variables
def sumNum(*args):
    sum=0
    #each passedargument will be storedin a list and now we are trying to work with list
    for i in range(len(args)):
        sum=args[i]+sum
    return sum
    
print("the first sum is:",sumNum(2,3))
print("the second sum is:",sumNum(1,2,3,4,5,6,7,8,9,10))
    


# In[60]:


#to pass arbitary number of variables
def sumNum(a,*args):
    sum=0
    print("the val of a is",a)
    #each passedargument will be storedin a list and now we are trying to work with list
    for i in range(len(args)):
        sum=args[i]+sum
    return sum
    
print("the first sum is:",sumNum(2,3))
print("the second sum is:",sumNum(1,2,3,4,5,6,7,8,9,10))
    


# In[55]:


#to pass arbitary number of variables
def sumNum(**args):
    sum=0
    for x in args:
        sum+=args[x]
    print(sum)
    
sumNum(a=2,b=3)
#print("the second sum is:",sumNum(1,2,3,4,5,6,7,8,9,10))
    


# In[68]:


#passing argument in different way
def sumNum(a,*b,**args):
    sum=0
    print("the value of a is :",a)
    for i in range(len(b)):
        print(b[i])
    for x in args:
        sum+=args[x]
    print(sum)
    
sumNum(1,"heloo","world",c=6,d=7,e=8,f=9,g=10)
    


# In[71]:


#Using default argment value
def sumN(a,b,c=8):
    sum=a+b+c
    print("the value of a,b,c respectively are",a,b,c)
    print(sum)
sumN(1,2,3)
sumN(1,2)
    


# In[52]:


def r():
    a=10
    b=23
    c='hai'
    return a,b,c


# In[46]:


x,y,z=r()
print(x,y,z)


# In[58]:


def printStrg(**args):
    for x in args:
        print(x,args[x])
printStrg(a="ANT",b="BALL",c="CAT")


# In[79]:


#passing list as argument
def ll(l=[1,2]):
    for i in range(len(l)):
        print(l[i])
ll()
ll([1,2,3])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




