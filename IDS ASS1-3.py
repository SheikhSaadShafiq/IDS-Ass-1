#!/usr/bin/env python
# coding: utf-8

# #                                            # Assignment # 1 

# In[ ]:





#                                             Question # 1
# 
# Write a Python program to convert temperatures to and from celsius, fahrenheit?
# 

#   
#  

# In[16]:


temp = float(input("Enter the temperature, which you want to convert:\t\t"))
#print(temp)
degree = input("The temperature you entered is in 'F' or 'C'\t\t\t")

#conversion
if degree == 'c' or degree == 'C':
    result = ((temp * 9)/5) + 32
    print("The temprature in Fahrenheit is :\t\t\t",result)
    
elif degree == 'F' or degree =='f':
    result = (temp - 32) * 5/9
    print("The temprature in Celsius is :\t\t\t", result)


#  
# 
#  
#                                         Question # 2

# Write a Python program to check if number is divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# 
# 

#     

# In[20]:


a = 1400

if(a/7) and (a%5==0) and (a>1500) and (a<2700):
    print("The number is divisible by 7 and multiple of 5, between 1500 and 2700 (both included).")
else:
    print("The number is 'NOT' divisible by 7 and multiple of 5, between 1500 and 2700 (both included).")


#                                         Question # 3
#                                         
# Use the list in the cell below and write a function to return the maximum and minimum value in the list. The function will take the list an argument and return two values.

# In[28]:


def maxmin(abc):
    N = [max(abc), min(abc)]
    return N


# In[31]:


A = [1,2,3,4,5,6,7,8,9]
result = maxmin(A)
print ("The Maximum number is\t\t\t",result[0],"\nThe Minimum number is\t\t\t",result[1] )


#                                         Question # 4
# Write a function to return the 2nd maximum and 2nd minimum value in the list. The function will take the list an argument and return two values

# In[46]:


def maxmin(abc):
    abc.sort()
    N = [abc[1], abc[-2]]
    print("The sorted list\t\t\t", abc)
    return N 


# In[47]:


A = [9,4,5,6,2,3,1,7,8,10,43,23,45,64,32,75]
result = maxmin(A)
print ("The 2nd Maximum number is\t\t\t",result[0],"\nThe 2nd Minimum number is\t\t\t",result[1] )


#                                         Question # 5
# Write a program to find the following statistics from a list. Note: Don’t use any built-in method for this question.
# • Mean
# • Median • Mode
# • Variance

# In[42]:


def mean(abc):
    range1 = len(abc)
    sum1 = sum(abc)
    total = sum1/range1
    return total


def median(abc):
    abc.sort()
    range1 = len(abc)
    a = int(range1 / 2)
    return abc[a]
    


# In[43]:


A = [9,4,5,6,2,3,1,7,8,10,43,23,45,64,32,75]
print("The mean of this list is : \t\t\t", mean(A))
print("The Median of this list is : \t\t\t", median(A))


#                                         Question # 6
#                                         
# You have three strings each containing different text, but all three have some common words in them. Your task is to find the frequency of words in each string and with the use of dictionary and list.
# The word will act as a 'key' in a dictionary where the value is a list containing the frequency of that word in all three strings.
# For example Dictionary['the'] -> List[] -> frequency count. the index '0' will contain the count of str1 and '1' will contain the count of str2 and so on. Following are the sample strings:
# 
# 
# • str1 = "a quick brown fox jumps over the lazy dog"
# 
# • str2 = "this course can be complex but not complicated if learnt properly"
# 
# • str3 = "the boeing plane max 8 was grounded all around the world for technical problems"
# 
# 

# In[3]:


import json

def CFwords(str_, word):
    splits = str_.split()
    freq = 0
    
    for x in splits:
        if x == word:
            freq = freq + 1
            
    return freq

def Commonwords_all(str1, str2, str3):
    s1_splits = str1.split()
    s2_splits = str2.split()
    s3_splits = str3.split()
    
    return list(set(s1_splits) | set(s2_splits) | set(s3_splits))

def Common_in_string(str_, comm_words):
    countList = []
    
    for x in comm_words:
        countList.append(CFwords(str_, x))
        
    return countList
        
def Commonwords(str1, str2, str3):
    comm_words = Commonwords_all(str1, str2, str3)
    print("Common words:", comm_words)
    
    freqList1 = Common_in_string(str1, comm_words)
    freqList2 = Common_in_string(str2, comm_words)
    freqList3 = Common_in_string(str3, comm_words)
    myDict = dict() 
    freqListLen = len(freqList1)
    
    for x, iterator in zip(comm_words, range(len(freqList1))):
        myDict[x] = []
        
        myDict[x].append(freqList1[iterator])
        myDict[x].append(freqList2[iterator])
        myDict[x].append(freqList3[iterator])
    
    return myDict

if __name__ == "__main__":
    
    str1 = "a quick brown fox jumps over the lazy dog"
    str2 = "this course can be complex but not complicated if learnt properly"
    str3 = "the boeing plane max 8 was grounded all around the world for technical problems"
    
    print(str1, "\n")
    print(str2, "\n")
    print(str3, "\n")

    result = Commonwords(str1, str2, str3)
    print("\n\nThe Result is : \n\t\t\t", result)


#                                             Question # 7
#     
# Write a program which will return ticket price for the following scenario

# In[1]:


import pandas as pd


# In[11]:


path = "/Users/saadshafiq/Downloads/Q7.csv"
df = pd.read_csv(path)
df.head(10)


# In[4]:


#tried to solve it with pandas but failed --> now going to do with if else 


# In[21]:


class Ticket:
    def __init__(self, day, status, entry_hrs, age):
        self.week_day = day
        self.visitor_status = status
        self.entry_hours = entry_hrs
        self.visitor_age = age
    
    def computeTicketPrice(self):
        days = {
            "working_days" : ["Mon", "Tue", "Wed", "Thus", "Fri"],
            "off_days" : ["Sat", "Sun"]
        }
        
        if self.week_day in days["working_days"]:
            
            if self.visitor_status == "OT":
                if self.entry_hours >= 6 and self.entry_hours <= 19:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 5
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 10
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 8
                    
                elif self.entry_hours >= 19.01 and self.entry_hours <= 24:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 6
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 12
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 8
                    
            elif self.visitor_status == "M":
                if self.entry_hours >= 6 and self.entry_hours <= 19:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 2.5
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 5
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 4
                    
                elif self.entry_hours >= 19.01 and self.entry_hours <= 24:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 3
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 6
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 4
                    
        elif self.week_day in days["off_days"]:
            
            if self.visitor_status == "OT":
                if self.entry_hours >= 6 and self.entry_hours <= 19:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 7.5
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 15
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 12
                    
                elif self.entry_hours >= 19.01 and self.entry_hours <= 24:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 9
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 18
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 12
                    
            elif self.visitor_status == "M":
                if self.entry_hours >= 6 and self.entry_hours <= 19:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 3.5
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 7
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 5.5
                    
                elif self.entry_hours >= 19.01 and self.entry_hours <= 24:
                    
                    if self.visitor_age >= 0 and self.visitor_age <= 16:
                        return 4
                    elif self.visitor_age >= 16.01 and self.visitor_age <= 60:
                        return 8
                    elif self.visitor_age >= 60.01 and self.visitor_age <= 120:
                        return 5.5
        
        return -1
temp_age = float(input("Enter the age:\t\t"))
print("\n\t\t\tWrite days in Mon, Tue, Wed, Thus, Fri, Sat, Sun\n")
temp_day = str(input("Enter the day:\t\t"))
temp_status = str(input("Enter your vistor status 'OT' or 'M':\t\t"))
temp_entryhour = int(input("Enter the entery hour:\t\t\t"))
if __name__ == "__main__":
    
    obj = Ticket(temp_day, temp_status, temp_entryhour, temp_age)
    ticket = obj.computeTicketPrice()
    
    if (ticket != -1):
        print("Ticket price:\t\t", ticket)
    else:
        raise Exception("\n\t\t\tError! Check again the parameters.")


# In[ ]:




