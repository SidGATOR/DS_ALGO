
# coding: utf-8

# In[36]:


class Queue(object):
    
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

        


# In[37]:


q = Queue()


# In[38]:


q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


# In[39]:


q.dequeue()


# In[40]:


q.dequeue()


# In[41]:


q.enqueue(4)


# In[42]:


q.enqueue(5)


# In[43]:


q.dequeue()


# In[44]:


q.isEmpty()


# In[45]:


q.size()


# In[ ]:




