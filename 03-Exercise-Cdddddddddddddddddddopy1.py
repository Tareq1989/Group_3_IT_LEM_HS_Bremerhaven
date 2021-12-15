#!/usr/bin/env python
# coding: utf-8

# # Exercice 1
# 
# Write a function called **string_to_array** to split a string and convert it into an array of words. The function should take one str argument and does not return anything, just print the array of words. 
# 
# For example:
# 
# ```python
# "Robin Singh" should return ["Robin", "Singh"]
# 
# "I love arrays they are my favorite" should return ["I", "love", "arrays", "they", "are", "my", "favorite"]
# ```
# 
# ### check your answer with the following strings 
# 
# `
# string_to_array("Robin Singh") should print ["Robin", "Singh"])
# string_to_array("CodeWars") should print ["CodeWars"]
# string_to_array("I love arrays they are my favorite") should print ["I", "love", "arrays", "they", "are", "my", "favorite"]
# string_to_array("1 2 3") should print ["1", "2", "3"]
# string_to_array("") should print [""]
# `

# In[51]:


def string_to_array(text):
   return text.split("")


# In[52]:


string_to_array("1 2 3")


# # Exercice 2: 
# 
# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# 
# Your task is to write a function called **maskify**, which changes all but the last four characters into '#' and return the value as a string (str).
# 
# Output example: 
# "What was the name of your first pet?"
# 
# ```python 
# maskify("Skippy")                                   == "##ippy"
# maskify("Nananananananananananananananana Batman!") == "####################################man!"
# ```
# 
# ### check your answer with the following strings 
# ```python 
# maskify("4556364607935616") == "############5616"
# maskify(     "64607935616") ==      "#######5616"
# maskify(               "1") ==                "1"
# maskify(                "") ==                 ""
# ```
# 
# 

# In[18]:


def maskify(text):
    maskified = ""
    if len(text)<4:
        return text

    for i in range(0,len(text)-4):
        maskified += "#"

    maskified += text[-4:]
    return (maskified)


# In[19]:


code = "455544555"
res = maskify(code)
print(res)


# # Exercice 3
# Your task is to create a function that does four basic mathematical operations.
# 
# The function should take three arguments - 
# 
# operation(string/char), 
# 
# value1(number), 
# 
# value2(number).
# 
# The function should return result of numbers after applying the chosen operation.
# 
# Examples
# ```python
# basic_op('+', 4, 7)         # Output: 11
# basic_op('-', 15, 18)       # Output: -3
# basic_op('*', 5, 5)         # Output: 25
# basic_op('/', 49, 7)        # Output: 7
# ```

# In[16]:


def basic_op(operation,value1,value2):
    if operation== "*" :
        return (value1 * value2)

    elif operation== "/" :
        return (value1/value2)

    elif operation== "-" :
        return (value1-value2)

    elif operation == "+" :
        return (value1+value2)


# In[17]:


res =basic_op("*",3,2)
print(res)


# # Exercice 4
# Who remembers back to their time in the schoolyard, when you would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
# 
# `
# I like you
# a little
# a lot
# passionately
# madly
# not at all
# `
# 
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# 
# 
# Your goal is to determine which phrase you would say for a flower of a given number of petals, where **nb_petals > 0**.
# 
# Examples: 
# 
# ```python
# how_much_i_like_you(7)         # Output: "I like you"
# how_much_i_like_you(2)         # Output: "a little"
# how_much_i_like_you(5)         # Output: "madly"
# how_much_i_like_you(9)         # Output: "a lot"
# ```
# 
# 

# In[29]:


def how_much_i_like_you(num):
    meaning = ["I like you","a little","a lot","passionatly","madly","not at all"]
    i = (num % 6)-1
    return meaning[i]


# In[30]:


res = how_much_i_like_you(5)
print(res)
res = how_much_i_like_you(7)
print(res)


# # Exercice 5 (slicing)
# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
# 
# For example:
# 
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
# 
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
# 
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
# 
# Note: Please remember that in python the index of an array starts at 0.
# 
# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
# 
# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.
# 
# Note:
# If you are given an array with multiple answers, return the lowest correct index.
# 
# Check your answer with the following arrays
# 
# `
# find_even_index([1,2,3,4,3,2,1]) should return 3
# find_even_index([1,100,50,-51,1,1]) should return 1
# find_even_index([1,2,3,4,5,6]) should return -1
# find_even_index([20,10,30,10,10,15,35]) should return 3
# find_even_index([20,10,-80,10,10,15,35]) should return 0
# find_even_index([10,-80,10,10,15,35,20]) should return 6
# find_even_index(range(1,100)) should return -1
# find_even_index([-1,-2,-3,-4,-3,-2,-1]) should return 3
# find_even_index(range(-100,-1)) should return -1
# find_even_index([0,0,0,0,0]) should return 0 because it Should pick the first index if more cases are valid
# `

# In[39]:


def find_even_index(array):
    j = -1
    k = 1
    for i in range(0,len(array)):
        j = j+1
        k = i+1
        left_side = array[:j]
        right_side = array[k:]
        sum_left = 0
        sum_right = 0
        for n in left_side:
            sum_left = sum_left+n
        for m in right_side:
            sum_right = sum_right+m
        if sum_right == sum_left:
            return j
    return -1


# In[50]:


find_even_index([0,0,0,0,0])


# # Exercice 6 
# You are given an input string.
# 
# For each symbol in the string if it's the first character occurence, replace it with a '1', else replace it with the amount of times you've already seen it...
# 
# Examples: 
# 
# ```python
# input   =  "Hello, World!"
# result  =  "1112111121311"
# 
# input   =  "aaaaaaaaaaaa"
# result  =  "123456789101112"
# ```
# 
# Test your code with the following strings
# 
# `
# numericals("Hello, World!")  should return  "1112111121311"
# numericals("Hello, World! It's me, JomoPipi!") should return "11121111213112111131224132411122"
# numericals("hello hello") should return  "11121122342"
# numericals("Hello") should return "11121"
# numericals("aaaaaaaaaaaa") should return "123456789101112"
# `

# In[ ]:


def numericals(text):
    chars = {}
    numeric = ""
    for i in text:
        if i in chars:
            chars[i] = chars[i] +1
        else:
            chars[i] = 1

        numeric = numeric + f"{chars[i]}"

    return (numeric)


# In[49]:


numericals("aaaaaaaaaaaa")


# # Exercice 7 
# 
# Write a function called 'solve'. It shoud take two arrays of string and return the number of times each string of the second array appears in the first array.
# 
# Example
# 
# array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
# 
# array2 = ['abc', 'cde', 'uap']
# 
# How many times do the elements in array2 appear in array1?
# 
# 
# 'abc' appears twice in the first array (2)
# 
# 'cde' appears only once (1)
# 
# 'uap' does not appear in the first array (0)
# 
# Therefore, solve(array1, array2) = [2, 1, 0]
# 
# 

# In[41]:


# your code here
def solve(array1,array2):
    frequency = []
    for i in range(0,len(array2)):
        frequency.append(0)
        for j in range(0,len(array1)):
            if array2[i] == array1[j]:
                frequency[i]+=1

    return frequency


# In[42]:



solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap']) 


# In[ ]:




