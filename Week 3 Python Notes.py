#!/usr/bin/env python
# coding: utf-8

# In[1]:


#install a library
import numpy as np


# In[2]:


my_list = [1,2,3]


# In[3]:


my_list


# In[4]:


np.array(my_list)


# In[6]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]


# In[7]:


my_matrix


# In[8]:


np.array(my_matrix)


# In[9]:


#arange
np.arange(0,10)


# In[10]:


#step by 2
np.arange(0,10,2)


# In[11]:


# zeros()
np.zeros(3)


# In[12]:


np.zeros((5,5))


# In[13]:


# ones()
np.ones(3)


# In[14]:


np.ones((3,3))


# In[15]:


#linspace()
#total of 3 numbers spaced evenly from 1-10
np.linspace(0,10,3) #This INCLUDES 10


# In[16]:


np.linspace(0,10,50)


# In[17]:


#eye(diag)
np.eye(4)


# In[18]:


#np.random()
np.random.rand(2)


# In[21]:


np.random.randn(5,5)


# In[20]:


#random integers from low (inclusive) to high (exclusive) range
np.random.randint(1,100,10)


# In[22]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10)


# In[23]:


arr


# In[24]:


ranarr


# In[26]:


arr.reshape(5,5)


# In[27]:


ranarr.max()


# In[28]:


#Where the max value exists
ranarr.argmax()


# In[29]:


ranarr.min()


# In[30]:


ranarr.argmin()


# In[31]:


arr.shape


# In[32]:


arr.reshape(1,25)


# In[33]:


arr.reshape(1,25).shape


# In[34]:


arr.reshape(25,1).shape


# In[35]:


np.mat(arr)


# In[36]:


arr.dtype


# In[38]:


arr = np.arange(25)


# In[39]:


arr[8]


# In[41]:


arr[1:5]


# In[42]:


arr[0:5] = 100
arr


# In[43]:


arr = np.arange(25)


# In[44]:


slice_arr = arr[0:6]
slice_arr


# In[45]:


slice_arr[:] = 99


# In[46]:


slice_arr


# In[47]:


#data is not copied into the slice, it is a view of arr
arr


# In[48]:


arr_copy = arr[0:6].copy()


# In[49]:


arr_copy


# In[51]:


arr2d = np.array(([5,10,15],[20,25,30],[35,40,45]))


# In[52]:


arr2d


# In[56]:


np.arange(5,46,5).reshape(3,3)


# In[57]:


arr2d[1]


# In[63]:


arr2d[:,0]


# In[59]:


#array[row,col];array[row][col]
arr2d[1,0]


# In[62]:


arr2d[:2,:2]


# In[64]:


arr2d = np.arange(1,101).reshape(10,10)


# In[65]:


arr2d


# In[66]:


arr2d[[0,2,4,6,8]]


# In[68]:


arr2d[[1,7,3, 2,8]]


# In[71]:


arr2d[:,[1,5,3,9]]


# In[72]:


arr2d[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
#elements (0,0), (1,1), (2,2), ...


# In[73]:


arr2d > 30


# In[74]:


arr2d * arr2d


# In[ ]:




