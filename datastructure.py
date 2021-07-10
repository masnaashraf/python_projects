#!/usr/bin/env python
# coding: utf-8

# In[9]:


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


# print(student_dict)
# 

# In[11]:


def getAvgMarks(d):
    avgmarks={}
    for x in d:
        l=d[x]
        s=0
        for marks in l:
            s+=int(marks)
        avgmarks[x]=s/len(l)  
    return avgmarks
avgMarksStudent=getAvgMarks(student_dict)
print(avgMarksStudent)
for x in avgMarksStudent:
    print("the average marks of student with id",x,"is",avgMarksStudent[x])


# In[6]:


print(student_dict)


# In[ ]:




