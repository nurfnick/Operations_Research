#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/nurfnick/Operations_Research/blob/main/SolvingSystems.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[3]:


import numpy as np

A = np.array([[3,2],[3,4]])
B = np.array([5,6])


# In[6]:


sol = np.linalg.solve(A,B)
sol


# In[9]:


np.matmul(A,sol)


# In[12]:


A @ sol


# In[ ]:




