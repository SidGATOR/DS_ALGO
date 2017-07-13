
# coding: utf-8

# In[1]:


class node(object):
    
    def __init__(self,data,next_node=None):
        self.element = data
        self.next_node = next_node


# In[26]:


class linklist(object):
    
    def __init__(self,head=None):
        self.head = head
    
    def insertNODE(self,data):
        new_node = node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def size(self):
        cnt = 0
        start = self.head
        while(start):
            cnt += 1
            start = start.next_node
        return cnt
    
    def search(self,data):
        current = self.head
        while(current):
            if (current.element == data):
                return current
            else:
                current = current.next_node
        raise ValueError("Data not in List")
    
    def deleteNODE(self,data):
        current = self.head
        previous = self.head
        if self.head.element == data:
            self.head = self.head.next_node
        else:
            while (current):
                if current.element == data:
                    previous.next_node = current.next_node
                    return
                else:
                    previous = current
                    current = current.next_node
            raise ValueError("Data item not in List")
    
    
                    
        
        


# In[27]:


lst = linklist()


# In[28]:


lst.insertNODE(1)


# In[29]:


lst.head.element


# In[30]:


lst.insertNODE(2)


# In[31]:


lst.head.element


# In[32]:


for i in range(3,11):
    lst.insertNODE(i)


# In[33]:


lst.head.element


# In[34]:


lst.size()


# In[35]:


lst2 = linklist()


# In[36]:


lst2.size()


# In[37]:


lst.search(5)


# In[38]:


lst.search(5).element


# In[41]:


lst.deleteNODE(1)


# In[42]:


lst.deleteNODE(10)


# In[43]:


lst.head


# In[44]:


lst.head.element


# In[45]:


lst.deleteNODE(9)


# In[46]:


lst.head.element


# In[47]:


lst.size()


# In[ ]:




