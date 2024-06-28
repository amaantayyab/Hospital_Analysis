#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv(r"C:\Users\amaan\Downloads\Business Analyst\netflixData.csv")


# In[30]:


#Let's find the movie with highest duration
data['Duration']


# In[31]:


data[['Time', 'Unit']] =data['Duration'].str.split(' ', expand = True)


# In[35]:


data.Time.dtype #we can't compare values if there of object datatype.


# In[42]:


data.head(2)


# In[38]:


data['Time'] = data['Time'].astype(float)
data['Time'].max()


# In[54]:


#Let's find out which country has the highest number of Tv Shows
data['Production Country'][(data['Content Type'] == 'TV Show')].value_counts().head(1)


# In[ ]:


#Let's sort the dataset by Year in descending order (The conventional sorting will be in aescending order)
data.sort_values('')

