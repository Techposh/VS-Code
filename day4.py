#!/usr/bin/env python
# coding: utf-8

# In[2]:


[i**2 for i in range(10)]


# In[3]:


[i for i in range(15)]


# In[4]:


range(15)


# In[8]:


from random import randint
[randint(1,100) for i in range(10)]


# In[18]:



myList = [1,2,3,4,5,6,7,8,9,10]
myList[9]


# In[21]:


myList[4] = 50
myList


# In[22]:


print(myList[4] * 100)


# In[23]:


len(myList)


# In[24]:


myList.append(500)


# In[25]:


myList


# In[27]:


x=10
y=2
myList.append(x*y**x)


# In[28]:


for value in myList :
    print(value)


# In[44]:


for i in range(len(myList)):
    if (i % 3 == 0) :
        myList[i] = 'deleted'
print(myList)

mylist=[1,2,3,4,5,6,7,8,9,10]
mylist.insert(4,4.5)
mylist
# In[39]:


mylist=[1,2,3,4,5,6,7,8,9,10]
mylist.insert(0,0.5)
mylist


# In[42]:


mylist.insert(6,[6.1,6.2,6.3])
mylist


# In[45]:


mylist[2]


# In[ ]:


str(mylist[2])


# In[47]:


mylist=[1,2,3,4,5,6,7,8,9,10]
mylist


# In[50]:


mylist.pop(0)
mylist


# In[51]:


mylist.pop(3)
mylist


# In[55]:


mylist.remove(6) # removes the first occurance of the value
mylist


# In[56]:


mylist=[1,2,3,4,5,6,7,8,9,10]


# In[ ]:


mylist=[1,2,3,3,4,5,3,2,6,7,6]


# In[57]:


mylist[4:7] # index 4 to 6, not including 7! in other words, 4 to 7 but not including 7


# In[58]:


mylist[5,0,2]
mylist


# In[61]:


mylist=[1,2,3,4]
names =["a","b","c"]
mixed=[1,2,"a"]
sum(mylist)

        


# In[63]:



from random import randint
mylist = [randint(1,10) in range(0,100)]
mylist


# In[64]:


mylist = [ randint(1,10) for i in range(0,100)]
mylist


# In[65]:


mylist = [ c for c in "this is my name scott thorthon"]
mylist.sort()


# In[66]:


mylist


# In[ ]:


randint(1,100)


# In[ ]:


for i in range(100) :
    print(randint(1,100))


# In[ ]:


mulist=[]
for i in range


# In[71]:


mylist = [randint(1,100) for i in range(7)]
mylist


# In[72]:


mylist = [ c for c in "scott"] # break into elements
mylist


# In[74]:


together = ""
for c in mylist : 
    together += c
together


# In[75]:


# get the input
grades = []

needInput = True

while needInput :
    userEntry = input("Enter a mark, empty line t othe end: ")
    if len(userEntry) == 0 :
        needInput = False
    else:
        grades.append(float(userEntry))
    
print(grades)
        


# In[87]:


# get the input
grades = []

needInput = True

while needInput :
    userEntry = input("Enter a mark, empty line t othe end: ").strip() # strip removes blank spaces from both end of the sentence
    if len(userEntry) == 0 :
        needInput = False
    else:
        grades.append(float(userEntry))
        
#Calculate mean median and mode

# mean
mean = sum(grades) / len(grades)

# median
grades.sort()
if len(grades) % 2 == 1 : # if the length is odd
    median = grades[int((len(grades)- 1) / 2)]

else:                     # if the length is even
    halfWay = int(len(grades) / 2)
    median = (grades[halfWay] + grades[halfWay - 1]) / 2

  
# mode
modeValue = grades[0]
modeFrequency = grades.count(grades[0])
for value in grades : 
    frequency = grades.count(value)
    if (frequency > modeFrequency) :
        modeValue = value
        modeFrequency = frequency


# output the results
print("The average is ", mean)
print("the median is  ", median)
print("the mode is ", modeValue, "and it occurs", modeFrequency, "times.")


# 2 % 3
# 

# In[91]:


# Exception Demo
maximum = 49
minimum = 1

needValue = True
while needValue :
    value = int(input("Enter value : "))
    if (value < minimum) or (value > maximum) :
        print ("Entered value is outside of range ", minimum, "to", maximum)
    else:
        needValue = False
        
print("Good value entered is ", value)


# In[92]:


# Exception Demo
maximum = 49
minimum = 1

needValue = True
while needValue :
    try :     #placing in exception
        value = int(input("Enter value : "))
        if (value < minimum) or (value > maximum) :
            print ("Entered value is outside of range ", minimum, "to", maximum)
        else:
            needValue = False
    except ValueError :
        print ("Enter non-numeric value. Please enter integers")
        
print("Good value entered is ", value)


# In[ ]:


baseLength = getValue("please enter the base of the trianlge", 0, 1000)
heigthLength = getValue("please enter the height of the triangle", 0, 1000)
area = baseLength * heigthLength * 0.5
print("traingle area is ", area)


# In[93]:


# Exception Demo
def getValue(prompt, minumum, maximum) :
    needValue = True
    while needValue :
        try :     #placing in exception
            value = int(input(prompt))
            if (value < minimum) or (value > maximum) :
                print ("Entered value is outside of range ", minimum, "to", maximum)
            else:
                needValue = False
        except ValueError :
            print ("Enter non-numeric value. Please enter integers")
    
    return value

baseLength = getValue("please enter the base of the trianlge", 0, 1000)
heigthLength = getValue("please enter the height of the triangle", 0, 1000)
area = baseLength * heigthLength * 0.5
print("traingle area is ", area)


# In[ ]:




