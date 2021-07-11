#!/usr/bin/env python
# coding: utf-8

# In[7]:


# creating a file and  writting into it
f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny.txt","w")
f.write("i love python")
f.close()


# In[8]:


# creating a file and  writting into it
f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny.txt","a")
f.write("I am learning itnow")
f.close()


# In[9]:


# creating a file and  writting into it
f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny.txt","a")
f.write("\nlearning is fun ")
f.close()


# In[16]:


# reading the whole file and printing the content
f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse.txt","r")
print(f.read())
f.close()


# In[17]:



f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse.txt","r")
#to read the contents of file line by line and print
for line in f:
    print(line)
f.close()


# In[18]:


#to read number of words in each line

f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse.txt","r")
#to read the contents of file line by line and print
for line in f:
    #converting each line into a list of words
    tokens=line.split(" ")
    print(str(tokens))
f.close()


# In[19]:


#to read number of words in each line

f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse.txt","r")
#to read the contents of file line by line and print
for line in f:
    #converting each line into a list of words
    tokens=line.split(" ")
    #gives word count in each line
    print(len(tokens))
f.close()


# In[26]:


#creating a new file and appending the word count of each line to it

f=open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse.txt","r")
#new file for writing
f_new=open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse_wc.txt","w")
#to read the contents of file line by line and print
for line in f:
    #converting each line into a list of words
    tokens=line.split(" ")
    
    #writing each line and appending word count to the new file
    f_new.write("\nwordcount:" + str(len(tokens))+" "+line)
f.close()
f_new.close()


# In[27]:


# reading the whole file and printing the content
f1=open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse_wc.txt","r")
print(f1.read())
f1.close()


# In[32]:


#if we are sing with statement then there is no need to have close() statement
# reading the whole file and printing the content
with open("C:/Users/Masna_2/Desktop/python/data analytics/funny_converse_wc.txt","r") as f:
    print(f.read())

print("checking whether the file is closed without f.close() statement")
print(f.closed) #gives you the status of file


# In[ ]:




