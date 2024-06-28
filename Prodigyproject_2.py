#!/usr/bin/env python
# coding: utf-8

# # Hospital Analysis

# # Loading the data

# In[55]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data= pd.read_csv(r"C:\Users\amaan\Desktop\April Challenge Dataset .csv")
data.head()


# # Understanding the data

# In[56]:


data.isnull().sum()


# Therefore, No Null values are present

# In[57]:


data.info()


# # Check for duplicate rows

# In[58]:


df = pd.DataFrame(data)
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")


# To drop the duplicate rows

# In[60]:


df.drop_duplicates(inplace=True)
duplicate_count = df.duplicated().sum
print(duplicate_count)



# # Summary

# In[61]:


df = pd.DataFrame(data)
df.columns = df.columns.str.strip()
df.drop(['Supplier Phone', 'Serial No'], axis=1, inplace=True)
summary=df.describe().round(2)
summary = summary.rename(index={
    'mean': 'Average value',
    'std': 'Standard Deviation',
    'min': 'Minimum value',
    'max': 'Maximum value'})
summary = summary.drop(['count','25%','50%','75%'])
summary


# # Handling unnecessary Columns

# In[62]:


df.columns = df.columns.str.strip()
df.drop([ 'Supplier Email', 'Supplier Contact'], axis=1, inplace=True)


# # Top 20 Hospitals by Order Quantity

# In[63]:


N = 20  
orders_per_hospital = df.groupby('Hospital')['Quantity'].sum().reset_index()
top_hospitals = orders_per_hospital.nlargest(N, 'Quantity')

plt.figure(figsize=(10, 6))
plt.bar(top_hospitals['Hospital'], top_hospitals['Quantity'], color='skyblue')
plt.xlabel('Hospital')
plt.ylabel('Total Quantity of Orders')
plt.title(f'Top {N} Hospitals by Order Quantity')
plt.xticks(rotation=90)
plt.show()


# # Number of Hospitals per Country

# In[64]:


hospitals_per_country = df.groupby('Supplier Country')['Hospital'].nunique().reset_index()
hospitals_per_country.columns = ['Supplier Country', 'Number of Hospitals']


plt.figure(figsize=(10, 6))
bars = plt.barh(hospitals_per_country['Supplier Country'], hospitals_per_country['Number of Hospitals'], color='skyblue')
plt.xlabel('Number of Hospitals')
plt.ylabel('Supplier Country')
plt.title('Number of Hospitals per Country that ordered Equipments')


for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, f'{width:.0f}', ha='left', va='center', color='blue')

plt.show()


# # Unique Equipments in each Department

# In[65]:


df['Department'] = df['Department'].str.strip()


unique_equipments_per_department = df.drop_duplicates(subset=['Hospital', 'Equipment']).groupby('Department').size().reset_index(name='Number of Unique Equipments')


plt.figure(figsize=(10, 6))
bars = plt.bar(unique_equipments_per_department['Department'], unique_equipments_per_department['Number of Unique Equipments'], color='skyblue')


for bar, qty in zip(bars, unique_equipments_per_department['Number of Unique Equipments']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{qty}', ha='center', va='bottom', fontsize=10)

plt.xlabel('Department')
plt.ylabel('Number of Unique Equipments')
plt.title('Number of Unique Equipments per Department (Grouped)')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# # Distribution of Hospitals per State 
# States with >=2% Hospitals

# In[66]:


hospital_counts = df['State'].value_counts()


total_hospitals = hospital_counts.sum()
hospital_counts_filtered = hospital_counts[hospital_counts / total_hospitals >= 0.02]

plt.figure(figsize=(8, 8))
plt.pie(hospital_counts_filtered, labels=hospital_counts_filtered.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# # Top 10 Costly Equipments

# In[67]:


df['Unit Price (USD)'] = pd.to_numeric(df['Unit Price (USD)'], errors='coerce')
df['Equipment with Department']= df['Equipment'] + '(' + df['Department'] + ')'

equipment_prices = df.groupby('Equipment with Department')['Unit Price (USD)'].mean().reset_index()
top_10_equipment_prices = equipment_prices.sort_values(by='Unit Price (USD)', ascending=False).head(10)
top_10_equipment_prices



# # Orders made by  Top Suppliers

# In[68]:


supplier_counts = df['Supplier'].value_counts().head(10)
supplier_counts = supplier_counts.reset_index()

plt.figure(figsize=(10, 6))
ax = sns.stripplot(x='Supplier', y='index', size=10, data=supplier_counts, palette='viridis', orient='h')

for i, count in enumerate(supplier_counts['Supplier']):
    ax.axhline(y=i, color='lightgrey', linestyle='--', linewidth=0.7, alpha=0.7)

plt.title('Number of Orders per Supplier')
plt.xlabel('Number of Orders')
plt.ylabel('Supplier')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# # Time taken to Deliver in each Department

# In[69]:


df['Date Ordered'] = pd.to_datetime(df['Date Ordered'])
df['Date Delivered'] = pd.to_datetime(df['Date Delivered'])

df['Delivery Time (Days)'] = (df['Date Delivered'] - df['Date Ordered']).dt.days

df['Department'] = df['Department'].str.strip()
plt.figure(figsize=(12, 6))
sns.violinplot(x='Department', y='Delivery Time (Days)', data=df, palette='viridis')
plt.title('Delivery Time Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Delivery Time (Days)')
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# # Average Waranty Period per Department

# In[70]:


df['Department'] = df['Department'].str.strip()

avg_warranty = df.groupby('Department')['Warranty Period (Years)'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(avg_warranty['Department'], avg_warranty['Warranty Period (Years)'], marker='o', linestyle='-', color='b')

plt.title('Average Warranty Period by Department')
plt.xlabel('Department')
plt.ylabel('Average Warranty Period (Years)')
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# # Average Insallation cost per Department

# In[71]:


df['Department'] = df['Department'].str.strip()

avg_maintenance = df.groupby('Department')['Installation Cost (USD)'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(avg_maintenance['Department'], avg_maintenance['Installation Cost (USD)'], marker='o', linestyle='-', color='b')

plt.title('Average Installation cost per Department')
plt.xlabel('Department')
plt.ylabel('Average Installation cost(USD)')
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# # Average Maintenance cost per Department

# In[72]:


df['Department'] = df['Department'].str.strip()

avg_maintenance = df.groupby('Department')['Maintenance Cost (USD/year)'].mean().reset_index()


plt.figure(figsize=(10, 6))
plt.plot(avg_maintenance['Department'], avg_maintenance['Maintenance Cost (USD/year)'], marker='o', linestyle='-', color='b')

plt.title('Average Maintenance cost per Department')
plt.xlabel('Department')
plt.ylabel('Average Maintenance cost(USD/year)')
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# # Distribution of Equipment

# In[73]:


equipment_condition_counts = df['Equipment Condition'].value_counts()

colors = ['#66b3ff', '#ff6666', '#99ff99']  # Bright Blue, Bright Red, Bright Green

plt.figure(figsize=(8, 8))
plt.pie(equipment_condition_counts, labels=equipment_condition_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'color':"Black",'fontsize':14})
plt.title('Percentage of New, Used, and Refurbished Equipment')
plt.axis('equal') 
plt.show()


# In[75]:


df.head()

