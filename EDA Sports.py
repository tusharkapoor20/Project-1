#!/usr/bin/env python
# coding: utf-8

# # Uploading CSV file

# In[12]:


import pandas as pd
import numpy as np


# In[13]:


import warnings
warnings.filterwarnings('ignore')


# In[14]:


df = pd.read_csv('fifa_eda_stats.csv')


# In[15]:


df.info()


# # Understanding the data

# In[16]:


df.describe()


# In[17]:


df.shape


# In[40]:


df.head()


# In[41]:


df.info()


# # Data Cleaning

# ### Changing the Data Type of some columns

# In[19]:


df['Value'].unique


# In[20]:


df['Value'] = df['Value'].str.replace('€','')
df['Value'] = df['Value'].str.replace('M','')
df['Value'] = df['Value'].str.replace('K','')
df['Value'] = df['Value'].astype(float)


# In[21]:


df['Value'].dtype


# In[22]:


df['Wage'] = df['Wage'].str.replace('€','')
df['Wage'] = df['Wage'].str.replace('M','')
df['Wage'] = df['Wage'].str.replace('K','')
df['Wage'] = df['Wage'].astype(float)


# In[23]:


df['Wage'].dtype


# In[24]:


df['Weight'].unique


# In[25]:


df['Weight'] = df['Weight'].str.replace('lbs','')
df['Weight'] = df['Weight'].astype(float)


# In[26]:


df['Weight'].dtype


# In[27]:


df['Release Clause'].unique


# In[28]:


df['Release Clause'] = df['Release Clause'].str.replace('€','')
df['Release Clause'] = df['Release Clause'].str.replace('M','')
df['Release Clause'] = df['Release Clause'].str.replace('K','')
df['Release Clause'] = df['Release Clause'].astype(float)


# In[29]:


df['Release Clause'].dtype


# ### Droping missing values

# In[30]:


print(df.isnull().sum())


# In[31]:


df.drop(['Loaned From'], axis=1,inplace =True)


# In[32]:


df = df.dropna(axis=0)
print(df.isnull().sum())


# ### Removing duplicates

# In[33]:


df.drop_duplicates(subset='ID', keep='first', inplace=True)


# # Visualising Data using Matplotlib 

# ### Histogram of Player Overall Ratings

# In[37]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('fifa_eda_stats.csv')

# Example 1: Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['Overall'], kde=True, color='skyblue')
plt.title('Histogram of Player Overall Ratings')
plt.xlabel('Overall Rating')
plt.ylabel('Frequency')
plt.show()


# ### Boxplot of Overall Ratings for Different Positions

# In[38]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Position', y='Overall', data=data, palette='coolwarm')
plt.title('Overall Ratings for Different Positions')
plt.show()


# ### Scatterplot of Overall Ratings vs Age with Nationality

# In[39]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Overall', data=data, hue='Nationality', palette='Set2', alpha=0.7)
plt.title('Overall Ratings vs. Age with Nationality')
plt.show()


# ### Heatmap to visualize the correlation between numeric variables

# In[45]:


plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


#  ### Scatter plot to explore the relationship between "Overall" vs "Potential"

# In[46]:


plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Overall', y='Potential', hue='Preferred Foot')
plt.title('Overall vs Potential Ratings')
plt.xlabel('Overall Rating')
plt.ylabel('Potential Rating')
plt.legend(title='Preferred Foot')
plt.show()


# In[ ]:




