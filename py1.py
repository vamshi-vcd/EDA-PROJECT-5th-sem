#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


# In[64]:


df=pd.read_csv("C:/Users/vamshi/desktop/final.csv")


# In[ ]:





# In[65]:


df.head(7)


# In[5]:


df.shape


# In[18]:


d=df[df.season <= 1983]
d


# In[21]:


plt.figure(figsize=(10,8))
sns.boxplot(data=d,x="weather_warm" ,y="round",hue="constructor")


# In[28]:


a=pd.pivot_table(data=df,index="constructor_wins",columns="driver_wins",values="qualifying_time")
a


# In[29]:


plt.figure(figsize=(10,8))
sns.heatmap(a,annot=True)


# In[34]:


b=pd.pivot_table(data=df,index="weather_cold",columns="driver_wins",values="qualifying_time")
b


# In[35]:


plt.figure(figsize=(10,8))
sns.heatmap(b,annot=True,cmap="PuRd")


# In[42]:


plt.figure(figsize=(10,8))
sns.heatmap(b,annot=True,cmap="Greens",center=1.5)


# In[44]:


plt.figure(figsize=(12,10))
sns.pairplot(data=df[["grid","driver_points","driver_wins"]])


# In[53]:


c=pd.pivot_table(data=df,index="weather_warm",columns="weather_cloudy",values="driver_wins")
c


# In[56]:


plt.figure(figsize=(10,8))
sns.heatmap(c,annot=True,cmap="Blues")


# In[ ]:




