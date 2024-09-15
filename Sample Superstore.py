#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from plotly.offline import iplot
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


df=pd.read_excel(r"C:\Users\cash\Desktop\Data Managment\SampleExemples - Superstore (1).xlsx")


# In[34]:


df


# In[35]:


df.shape


# In[36]:


df.dtypes


# In[37]:


df.head()


# In[38]:


df.isnull().sum()


# In[39]:


df.isna().sum()
df.dropna


# In[40]:


df.info()
df.describe()


# In[41]:


df.corr()


# In[42]:


df.corr()
sns.heatmap(df.corr())


# In[43]:


df['Sub-Category'].value_counts()


# In[45]:


plt.figure(figsize=(8,5))
sns.countplot(x=df['Ship Mode'])


# In[46]:


plt.figure(figsize=(8,6))
sns.countplot(x=df['Segment'])
plt.show()


# In[49]:


plt.figure(figsize=(20,8))
sns.countplot(x=df['City'], order=(df['City'].value_counts().head(50)).index)
plt.xticks(rotation=90)


# In[50]:


plt.figure(figsize=(20,8))
sns.countplot(x=df['State'])
plt.xticks(rotation=90)


# In[51]:


plt.figure(figsize=(20,8))
sns.countplot(x=df['Sub-Category'])
plt.xticks(rotation=90)


# In[52]:


plt.figure(figsize=(20,8))
sns.barplot(x=df['Sub-Category'], y=df['Profit'])
plt.xticks(rotation=90)


# In[55]:


plt.figure(figsize=(20,8))
sns.barplot(x=df['State'], y=df['Profit'])
plt.xticks(rotation=90)


# In[57]:


plt.figure(figsize=(20,8))
sns.barplot(x=df['Region'], y=df['Profit'])
plt.xticks(rotation=90)


# In[58]:


plt.figure(figsize=(20,8))
sns.barplot(x=df['Category'], y=df['Profit'])
plt.xticks(rotation=90)


# In[59]:


plt.figure(figsize=(20,8))
sns.barplot(x=df['Segment'], y=df['Profit'])
plt.xticks(rotation=90)


# In[62]:


#Highest ordered Product
df2=df.groupby(['Category','Sub-Category'])['Quantity'].sum().sort_values(ascending=False)
z=df2.plot(kind='bar',xlabel=('Subcategory with Category'),ylabel=('Ordered Quantity'))
plt.title('Ordered Quantities of each subcategory')
plt.figure(figsize=(15,8))
plt.show()
     


# In[68]:


#Profit/loss based on subcategory
df.groupby(['Category','Sub-Category'])['Profit'].sum().plot(kind='barh', figsize=(15,10),title="Profit/loss based on Product")


# In[70]:


df.groupby("Region")["Sales"].sum().plot.pie(autopct="%1.1f%%")


# In[71]:


df.groupby("Segment")["Sales"].sum().plot.pie(autopct="%1.1f%%")


# In[72]:


df.groupby("Category")["Profit"].sum().plot.pie(autopct="%1.1f%%")


# In[74]:


#Total quantity of items sold in each state
plt.figure(figsize=(13,13))
df.groupby("State")["Quantity"].sum().plot.bar()


# In[75]:


plt.ylabel("Count")
df["Ship Mode"].value_counts().plot.bar()


# In[76]:


print(df["Profit"].sum())
print(df["Discount"].sum())
print(df["Sales"].sum())


# In[77]:


sales_by_category = df[['Category', 'Sales']].groupby(['Category']).sum()
sales_by_category.head()


# In[78]:


sales_by_region = df[['Region', 'Sales']].groupby(['Region']).sum()
sales_by_region.head()


# In[80]:


sales_by_subcategory = df[['Sub-Category', 'Sales']].groupby(['Sub-Category']).sum()
sales_by_subcategory.head()


# In[ ]:




