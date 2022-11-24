#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Reading the Dataset

# In[11]:


df=pd.read_csv("final.csv")
df.head()


# ## Data cleaning
# ### Finding null values in data
# 

# In[8]:


df.isna().sum()


# ## Univariate unordered analysis
# 

# In[16]:


df.driver_age.value_counts()


# In[18]:


plt.figure(figsize=(10,8))
df.driver_age.value_counts(normalize=True).plot.barh(color="orange",edgecolor="black")
plt.show()


# In[21]:


plt.figure(figsize=(10,8))
df.grid.value_counts(normalize=True).plot.barh(color="blue",edgecolor="red")
plt.show()


# # Box Plot

# In[23]:


plt.figure(figsize=(10,8))
sns.boxplot(df["podium"],color="yellow")


# ### This Boxplot tells us the mean value of podiun number is approximately 12

# In[24]:


df["driver_age"].median()


# In[25]:


df.describe()


# ## Univariate ordered analysis

# In[27]:


plt.figure(figsize=(10,8))
df[df.driver_age >= 36 ].driver_age.value_counts().plot.pie()
plt.legend()


# In[29]:


plt.figure(figsize=(10,8))
df[(df.driver_age < 35) & (df.driver_age > 28)].driver_age.value_counts().plot.pie()
plt.legend()


# ## Bivariate analysis

# In[33]:


plt.figure(figsize=(10,8))
plt.scatter(df.driver_age,df.season,color="orange")
plt.show()


# In[40]:


plt.figure(figsize=(10,8))
plt.scatter(df.season,df.driver_wins,color="green")
plt.show()


# ## Correlation Map

# In[43]:


plt.figure(figsize=(10,8))
sns.heatmap(df[["driver_age","season","podium","qualifying_time","grid"]].corr(),annot=True)


# In[44]:


df.groupby("season")["driver_age"].mean()


# In[45]:


df.groupby("season")["driver_age"].median()


# # Stastical Analysis

# In[47]:


df.describe()


# In[48]:


df.driver_age.describe()


# In[49]:


df.podium.describe()


# In[50]:


df.grid.describe()

