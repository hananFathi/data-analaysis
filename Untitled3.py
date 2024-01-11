#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
filepath=r"C:\Users\hanan\Downloads\dailyActivity_merged.csv"
data=pd.read_csv(filepath)
data


# In[6]:


import matplotlib.pyplot as plt
y=data['VeryActiveDistance']
x=data['ActivityDate']
plt.plot(x,y)
plt.xticks(rotation=-50)
plt.show()


# In[7]:


#most active day is 5/30/2016


# In[9]:


import matplotlib.pyplot as plt
y=data['SedentaryMinutes']
x=data['ActivityDate']
plt.plot(y,x)
plt.xticks(rotation=-50)
plt.show()


# In[ ]:




