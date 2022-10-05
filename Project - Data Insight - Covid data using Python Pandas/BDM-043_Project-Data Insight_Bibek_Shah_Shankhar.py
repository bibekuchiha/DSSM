#!/usr/bin/env python
# coding: utf-8

# ## Project - Data Insight - Covid data using Python Pandas
# 
# Student Name - Bibek Shah Shankhar
# 
# Student Id - C0835648
# 
# Subject - BDM 1043 - Big Data Fundamentals 
# 
# 
# 
# ### Questions Solved
# 
# 1. Which Group have the most covid outbreaks from 2020-10-11 to 2021-11-28 ?
# 2. Which Sub-Group have the most covid outbreaks from 2020-10-11 to 2021-11-28 ?
# 3. From 2021 November, which group is rising most ?
# 4. From last 6 months, which group is rising most ?
# 5. which group has most number of covid outbreak in first 6 months of 2021 ?

# In[80]:


#Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[81]:


#Loading dataset using Pandas
'''
This dataset is from 
2020-11-01 to 2021-11-28
'''
df = pd.read_csv('ongoing_outbreaks.csv')

#Printing top 5 rows
df.head()


# In[82]:


#checking null values
df.isnull().sum()


# In[83]:


#Checking the shape of our dataset
df.shape


# There are 8744 rows and 4 columns in our dataset

# In[84]:


#Checking the date range in our dataset
df.date.unique()


# Calculating the sum of total ongoing outbreaks from 2020-11-01 to 2021-11-28

# In[85]:


df.number_ongoing_outbreaks.sum()


# We can see there are 188907 outbreaks between 2020-11-01 to 2021-11-28

# We are listing the groups category from our dataset from which covid outbreak is recorded

# In[86]:


for i in (df.outbreak_group.unique()):
    print(i)


# We are listing the subgroups category from our dataset from which covid outbreak is recorded

# In[87]:


for i in df.outbreak_subgroup.unique():
    print(i)


# In[88]:


#Displaying last 10 results
df.tail(10)


# We are plotting the count of outbreak_group 

# In[89]:


df.outbreak_group.value_counts().plot(kind='bar');


# In[90]:


df.outbreak_subgroup.value_counts().plot(kind='bar');


# We are creating new datafame to store only two columns outbreak and number_ongoing_outbreak

# In[91]:


new_df = df[['outbreak_group','number_ongoing_outbreaks']]
#printing top 5 results
new_df.head()


# ## QUESTION:
# ### 1. Which Group have the most covid outbreaks from 2020-10-11 to 2021-11-28 ?

# From the overall dataset from date 2020-11-1 to 2021-11-28 , We are grouping our outbreak group to Ongoing number of covid outbreaks and sorting the numbers in descending order

# In[92]:


most_covid_outbreak_group = df.groupby('outbreak_group')['number_ongoing_outbreaks'].sum().sort_values(ascending=False) 
most_covid_outbreak_group


# In[93]:


#ploting the group with covid outbreak
most_covid_outbreak_group.plot(kind='barh')


# From the above statistics we can see that, The most number of covid outbreak group is From Workplace group and Also Congregate Care also have almost same number with little difference in number. And Education is also rising

# ## QUESTION:
# ### 2. Which Sub-Group have the most covid outbreaks from 2020-10-11 to 2021-11-28 ?
# 
# 

# In[94]:


most_covid_outbreak_subgroup = df.groupby('outbreak_subgroup')['number_ongoing_outbreaks'].sum().sort_values(ascending=False)        
#listing covid outbreak subgroup with numbers
most_covid_outbreak_subgroup


# In[95]:


#ploting the subgroup with covid outbreak
most_covid_outbreak_subgroup = df.groupby('outbreak_subgroup')['number_ongoing_outbreaks'].sum().plot(kind='bar')


# In this above statistics too we can see that, The most number of covid outbreak group is From Workplace group .And Covid outbreak at Educational sector is also rising

# # Question
# ### 3. From 2021 November, which group is rising most ?
# 
# From the overall dataset  date 2021 nov to 28 Nov , We will be grouping our outbreak group to Ongoing number of covid outbreaks and sorting the numbers in descending order.
# 
# Firslty we are creating a new dataframe which starts from 2021 nov

# In[96]:


#Creating a new dataframe where date is greater than 2021-10-31 which starts from Nov 2021
date_from_2021 =  df[df['date'] > '2021-10-31']


# In[97]:


#listing top 5 headers
date_from_2021.head()


# In[98]:


date_from_2021.tail()


# In[99]:


nov_2021_outbreak_subgroup = date_from_2021.groupby('outbreak_subgroup')['number_ongoing_outbreaks'].sum().sort_values(ascending=False)        
#listing all results
nov_2021_outbreak_subgroup


# In[100]:


#plotting vertical graph for nov 2021 outbreak subgroup
nov_2021_outbreak_subgroup.plot(kind='bar')


# Now we are grouping our outbreak_group in terms of number of covid outbreaks ongoing and plotting the results

# In[101]:


#plotting vertical graph for nov 2021 outbreak group
nov_2021_outbreak_group = date_from_2021.groupby('outbreak_group')['number_ongoing_outbreaks'].sum().plot(kind='barh')
nov_2021_outbreak_group


# We can see that the covid cases in educational sectors is rising rapidly due to opening of schools and colleges which is needed to take control and the cases in workplace group is in 2nd position with huge gap between education

# # Question
# ### 4.  From last 6 months, which group is rising most ?

# In[102]:


last_six_months =  df[df['date'] > '2021-06-31']
last_six_months.head()


# In[103]:


last_six_months_group = last_six_months.groupby('outbreak_group')['number_ongoing_outbreaks'].sum().plot(kind='barh')
last_six_months_group


# Here from this chart we can see it clearly now that the covid outbreak in education sector is the group which is growing the most covid cases in ontario , Canada

# # Question
# ### 5. which group has most number of covid outbreak in first 6 months of 2021 ?

# In[104]:


first_six_months =  df[(df['date'] < '2021-06-31') & (df['date'] > '2020-12-31')]
#printing first 5 headers
first_six_months.head()


# In[105]:


first_six_months['date'].unique()


# We can see that, our date starts from 2021-01 upto 2021-06-31 which is first 6 months data

# In[106]:


first_6months_outbreak_group = first_six_months.groupby('outbreak_group')['number_ongoing_outbreaks'].sum()
first_6months_outbreak_group


# In[107]:


first_6months_outbreak_group.plot(kind='barh')


# we can see that, covid cases in workplace and congregate care are with the most number and education is in 3rd position which will top up in next 6 months
# 
# ##### Conclusion
# We can see that, in the first 6 months of 2021 , Workplace and Congregate care were dominating the most covid cases while education was slowly rising and after 6 months, the covid cases in the education jumps rapidly with a strong pace which tops the group in last 6 months and recenlty till this date, this group is still dominating the race which needs to be controlled .
