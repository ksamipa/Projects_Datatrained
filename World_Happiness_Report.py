#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')


# In[9]:


df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')


# In[10]:


type(df)


# In[11]:


df


# In[12]:


df.head(11)


# In[13]:


df.tail(2)


# In[14]:


df.sample()


# In[15]:


type(df.columns)


# In[16]:


df.columns


# In[17]:


df.isnull().sum()


# In[18]:


import seaborn as sns


# In[19]:


sns.scatterplot()


# In[20]:


sns.scatterplot(x='Dystopia Residual', y='Country', data=df)


# In[21]:


sns.scatterplot(x='Dystopia Residual', y='Region', data=df)


# In[22]:


sns.scatterplot(x='Dystopia Residual', y='Happiness Rank', data=df)


# In[23]:


sns.scatterplot(x='Dystopia Residual', y='Happiness Score', data=df)


# In[24]:


sns.scatterplot(x='Dystopia Residual', y='Standard Error', data=df)


# In[25]:


sns.scatterplot(x='Dystopia Residual', y='Economy (GDP per Capita)', data=df)


# In[26]:


sns.scatterplot(x='Dystopia Residual', y='Family', data=df)


# In[27]:


sns.scatterplot(x='Dystopia Residual' , y= 'Health (Life Expectancy)', data=df)


# In[28]:


sns.scatterplot(x='Dystopia Residual' , y= 'Trust (Government Corruption)', data=df)


# In[29]:


sns.scatterplot(x='Dystopia Residual' , y= 'Freedom', data=df)


# In[30]:


sns.scatterplot(x='Dystopia Residual' , y= 'Generosity', data=df)


# In[31]:


import matplotlib.pyplot as plt
sns.pairplot(df)
plt.savefig('pairplot.png')
plt.show()


# In[32]:


df.corr()


# In[33]:


df.corr()['Dystopia Residual'].sort_values()


# In[ ]:




