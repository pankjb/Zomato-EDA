#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matlpotlib', 'inline')


# In[6]:


df = pd.read_csv('zomato.csv', encoding = 'latin-1')


# In[7]:


df.head()


# In[14]:


df.shape


# In[8]:


df.columns


# In[12]:


df.info()


# In[11]:


df.describe()


# In[ ]:


## Data Analysis
1. Missing Values
2. Explore Numerical Values
3. Explore Categorical Values
4. Find relation between features


# In[13]:


df.isnull().sum()


# In[16]:


[features for features in df.columns if df[features].isnull().sum() > 0]


# In[48]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.heatmap(df.isnull(), yticklabels = False, cbar = False, cmap = 'viridis')


# In[20]:


df_country = pd.read_excel('Country-Code.xlsx')


# In[22]:


df_country.head()


# In[23]:


df.columns


# In[24]:


final_pd = pd.merge(df,df_country, on = 'Country Code', how = 'left')


# In[25]:


final_pd.head()


# In[28]:


final_pd.dtypes


# In[31]:


final_pd.columns


# In[32]:


final_pd.Country.value_counts()


# In[33]:


country_names = final_pd.Country.value_counts().index


# In[34]:


country_val = final_pd.Country.value_counts().values


# In[39]:


#Pie Chart - Top 3 countries
plt.pie(country_val[:3], labels = country_names[:3], autopct = '%1.2f%%')


# In[ ]:


Observation: India contributes chunk of transactions followed by usa, uk


# In[41]:


final_pd.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size()


# In[42]:


final_pd.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index()


# In[44]:


ratings = final_pd.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[45]:


ratings


# In[ ]:


## Observations
1. >4.5: Excellent
2. 4-4.5: VG
3. 3.5 - 3.9: G
4. So on


# In[47]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x = 'Aggregate rating', y = 'Rating Count', data = ratings)


# In[52]:


sns.barplot(x = 'Aggregate rating', y = 'Rating Count', hue = 'Rating color', data = ratings)


# In[53]:


sns.barplot(x = 'Aggregate rating', y = 'Rating Count', hue = 'Rating color', data = ratings, palette = ['white', 'red', 'orange', 'yellow', 'green', 'green'] )


# In[ ]:


## Observations
1. Not rated count is very high
2. max range is from 2.4 to 4.4


# In[54]:


sns.countplot(x = 'Rating color', data = ratings, palette = ['blue', 'red', 'orange', 'yellow', 'green', 'green'])


# In[57]:


#Countries that has given 0 Ratings
final_pd[final_pd['Rating color']=='White'].groupby('Country').size().reset_index


# In[ ]:


## Observations
1. Max no. of 0 ratings are from India


# In[59]:


final_pd.columns


# In[73]:


final_pd[['Currency','Country']].groupby(['Country','Currency']).size().reset_index()
                                        


# In[72]:


final_pd[['Country','Has Online delivery']].groupby(['Country','Has Online delivery']).size().reset_index()


# In[69]:


final_pd[final_pd['Has Online delivery'] == 'Yes'].Country.value_counts()


# In[ ]:


## Create Flow Chart for Top 5 Cities


# In[79]:


final_pd.City.value_counts().index


# In[83]:


city_values = final_pd.City.value_counts().values
city_labels = final_pd.City.value_counts().index


# In[85]:


plt.pie(city_values[:5],labels = city_labels[:5], autopct = '%1.2f%%')


# In[ ]:




