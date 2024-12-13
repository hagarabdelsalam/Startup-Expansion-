#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[41]:


data= pd.read_csv(r"C:\Users\Online\Downloads\is project\P1-StartupExpansion2.csv")
#df
data = data.set_index('Store ID')
data


# In[80]:


# Line Plot
plt.plot(data['Sales Region'], data['Revenue'],  marker='o', label='Revenue vs Sales Region',alpha=0.5,ls='--')
plt.title('Line Plot: Sales Region vs Revenue')
plt.xlabel('Revenue')
plt.ylabel('Sales Region')
plt.show()


# In[74]:


# Bar Chart
plt.figure(figsize=(10, 6))
data.groupby('State')['Revenue'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Bar Chart: Total Revenue by State',fontsize=20)
plt.ylabel('Total Revenue',fontsize=15)
plt.xlabel('State',fontsize=15)
plt.xticks(rotation=77)
plt.show()


# In[65]:


# Scatter Plot
plt.scatter(data ['Marketing Spend'], data['Revenue'])
plt.title('Scatter Plot: Marketing Spend vs Revenue',fontsize=20)
plt.xlabel('Marketing Spend',fontsize=15)
plt.ylabel('Revenue',fontsize=15)
plt.show()


# In[66]:


# Histogram
plt.hist(data['Revenue'], bins=15,color='orange', edgecolor='black')
plt.title('Histogram: Distribution of Revenue',fontsize=20)
plt.xlabel('Revenue',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.show()


# In[100]:


# Plot the Pie Chart

# Choose a column for grouping (e.g., 'New Expansion')
category_counts = data['New Expansion'].value_counts()

# Plot Pie Chart using the dataset
plt.figure(figsize=(6, 6))
plt.pie(
    category_counts, 
    labels=category_counts.index, 
    autopct='%1.1f%%',  # Show percentages
    startangle=140     # Rotate the pie chart
)
plt.title('Distribution of New Expansion',fontsize=20)
plt.show()


# In[104]:


# Choose a column for grouping (مثلاً 'New Expansion')
category_counts = data['New Expansion'].value_counts()

# Labels (الفئات)
labels = category_counts.index

# رسم الـ Donut Chart
plt.figure(figsize=(6,6 ))
plt.pie(
    category_counts, 
    labels=labels, 
    autopct='%1.1f%%',  # عرض النسبة المئوية
    startangle=140
)
plt.axis('equal')  # يجعل الدائرة متساوية

# إضافة دائرة بيضاء لعمل التأثير الدائري (Donut)
circle = plt.Circle((0, 0), 0.75, color='white')
plt.gca().add_artist(circle)

# إضافة عنوان
plt.title("Distribution of New Expansion", loc='center', color='black', fontsize=20, fontweight='bold')

# عرض الرسم
plt.show()


# In[ ]:




