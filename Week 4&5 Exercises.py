#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
import os
import numpy as np
import pandas as pd


# In[3]:


os.getcwd()


# In[5]:


#Read in peanut_lines
peanut_lines = pd.read_csv('peanut_lines.csv', encoding='ISO-8859-1')


# In[6]:


#Check head of files
peanut_lines.head()


# In[8]:


#Number of peanut_lines
peanut_lines.info()
#Number of unique entries
peanut_lines['NC_Accession'].nunique()


# In[10]:


#read in peanut_yield
peanut_yield = pd.read_csv('peanut_yield.txt', sep='\t', encoding='ISO-8859-1')


# In[13]:


#Get column names for peanut_yield
list(peanut_yield.columns.values)


# In[16]:


#Merge data frames on NC_Accession keeping all of peanut_yield (Left outer join)
peanut_data = pd.merge(peanut_yield, peanut_lines, how = 'left', on = 'NC_Accession')


# In[21]:


#Group by year and get means
by_year = peanut_data.groupby('Year')
by_year.mean()


# In[31]:


#Sort by yield
descending = peanut_data.sort_values(by='Yield', ascending=False)
top10 = descending.head(10)
#Get mean yield of top 10 lines
top10['Yield'].mean()


# In[39]:


#value_counts by accession
list_top = peanut_data['NC_Accession'].value_counts()
common10 = list_top.head(10)


# In[53]:


#Create new df with subset of data that match conditions
line_data = peanut_data[((peanut_data['Location']=='LEW')|(peanut_data['Location'] == 'RMT'))&((peanut_data['NC_Accession']=='Bailey')|(peanut_data['NC_Accession']=='Sullivan')|(peanut_data['NC_Accession']=='Wynne')|(peanut_data['NC_Accession']=='Emery')|(peanut_data['NC_Accession']=='Bailey II')|(peanut_data['NC_Accession']=='N14023'))]


# In[56]:


#groupby accession and get means
line_means = line_data.groupby('NC_Accession').mean()


# In[57]:





# In[59]:


#Export to excel
line_means.to_excel('NCSU_release.xlsx', index=False)


# In[ ]:




