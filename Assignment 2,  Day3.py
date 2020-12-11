#!/usr/bin/env python
# coding: utf-8

# # Question 1.
# Use IF ELSE and Elif to write a program in pythn for your reportcard

# In[5]:


marks = 36
if marks > 90 and marks <= 100:
    print ("Grade -> A+")
elif marks > 80 and marks <= 90:
    print("Grade -> A")
elif marks > 70 and marks <= 80:
    print("Grade -> B+")
elif marks > 60 and marks <= 70:
    print("Grade -> B")
elif marks > 50 and marks <= 60:
    print("Grade -> C+")
elif marks > 40 and marks <= 50:
    print("Grade -> C")
else: 
    print("Fail")

    


# ---

# # Question 2.
# Use for loop to print Prime Number in Between 1 to 1000

# In[8]:


for Num in range (1,101):
    count = 0
    for i in range(1,Num+1):
        if(Num % i == 0):
            count = count + 1
    if(count == 2):
        print(Num, end = "   ")


# ----

# # Question 3.
# Write a program for printing the tble from 1, 10 using nested for loop

# In[12]:


Num = int(input("Enter the number: "))

print("Multipication Table of", Num)
for i in range(1, 11):
    print(Num,"X",i, "=",Num*i)


# ----

# # Question 4.
# Write a programe to print X prime Numbers using while loop starting from 0, and take the input of X from the user
# 

# In[9]:


Num = int(input("Please Enter any Number: "))
count = 0
i = 2

while (i<= Num//2):
    if(Num %i == 0 ):
        count = count + 1
        break
    i = i +1
if (count == 0 and Num != 1):
    print(" %d is a Prime Number" %Num)
else:
    print(" %d is not a Prime Number" % Num)


# In[ ]:




