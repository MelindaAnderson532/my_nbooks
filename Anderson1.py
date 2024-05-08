#!/usr/bin/env python
# coding: utf-8

# # Exercise 1-1: Get started with JupyterLab

# ## Get the data

# # Melinda Anderson

# ## Phases of Analysis and Visualization

# 1. Get the data
# 2. Clean the data
# 3. Prepare the data
# 4. Analyze the data
# 5. Visualize the data

# In[1]:


import pandas as pd
poll_url = 'http://projects.fivethirtyeight.com/general-model/president_general_polls_2016.csv'
polls = pd.read_csv(poll_url)


# In[3]:


polls.head()


# In[7]:


polls.sort_values('state', inplace=True)
polls.head(2)


# ## Use Tab completion and tooltips

# In[10]:


polls.sort_values('state', ascending=False)
polls.head()


# ## Clean the data

# ### Keep only the rows with "now-cast" in the type column

# In[11]:


polls = polls.query('type=="now-cast"')
polls.head()


# ### Rename voting columns

# In[13]:


polls.rename(columns={'rawpoll_clinton':'Clinton_pct',
                      'rawpoll_trump':'Trump_pct'},inplace=True)
polls.head()


# ### Convert date columns to datetime objects

# In[14]:


date_cols = ["startdate","enddate"]
polls[date_cols] = polls[date_cols].apply(pd.to_datetime)
polls.head()


# ### Try two plots

# In[15]:


polls.plot.line(x='enddate',y=['Clinton_pct','Trump_pct'])


# In[17]:


get_ipython().run_cell_magic('time', '', 'polls.query(\'state == "U.S."\') \\\n    .plot(x=\'enddate\',y=[\'Clinton_pct\',\'Trump_pct\'])\n')


# In[18]:


get_ipython().run_line_magic('whos', '')


# In[21]:


type(polls)


# In[ ]:




