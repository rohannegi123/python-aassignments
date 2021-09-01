#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# ## Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# # area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# # Function to take the length of the sides of triangle from user should be defined in the parent .class and function to calculate the area should be defined in subclass.

# In[75]:


class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
class triangle_sides(triangle):
    def __init__(self, a ,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s=(self.a + self.b + self.c )
        return  (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        
area_t = triangle_sides(1,2,3)
area_t.area()


# In[72]:





# # 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[77]:


class filterwords:
    def __init__(self,words ,n):
        self.words = words
        self.n = n
        
    def filter_long_words(self):
        a = []
        for i in self.words:
            if len(i) > self.n  :
                a.append(i)    
        return a
    
    
a = filterwords(['rohan' , 'negi' , 'to' , 'on' , 'amar'] ,2)
a.filter_long_words()


# In[ ]:





# # 2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# # Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# # Here 2,3 and 4 are the lengths of the words in the list.

# In[80]:


class listofwords:
    def __init__(self,words):
        self.words = words
        
    def represntlength(self):
        a = []
        for i in self.words:
            a.append(len(i))
            
        return a


a = listofwords(['rohan','negi' , 'rahul' , 'ineuron' , 'sudhansu'])
a.represntlength()


# In[ ]:





# # 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# In[313]:


class string:
    def __init__(self,word):
        self.word = word 
        if len(word) > 1:
            print('please enter str of len 1')
            
            
        
    def vowel_or_not(self):
        if len(self.word) == 1:
            vowels =('a' , 'e' , 'i' , 'o' ,'u')
            if self.word not in vowels:
                     return False
            else:
                     return True
        else :
            print('str of higher then len = 1 was given')
        
            


# In[315]:


a = string('a3')
a.vowel_or_not()


# In[317]:


b = string('r')
b.vowel_or_not()


# In[319]:


c = string('e')
c.vowel_or_not()


# In[ ]:





# In[ ]:





# In[ ]:




