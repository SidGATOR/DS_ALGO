
# coding: utf-8

# In[1]:


class node(object):
    
    def __init__(self,data,next_node=None,prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


# In[61]:


class dlist(object):        
    
    def __init__ (self,head=None,tail=None):
        self.head = head
        self.tail = tail
    
    def insertNODE(self,data):
        if self.head == None:
            new_node = node(data)
            self.head = self.tail = new_node
        else:
            new_node = node(data)
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
    
    def deleteNODE(self,node_value):
        tmp = self.head
        ### Check if list is empty ###
        if (self.size() == 0):
            raise ValueError("List is empty")
        else:
            ### Check for head ###
            if (self.head.data == node_value):
                self.head = self.head.next_node
            elif (self.tail.data == node_value):
                self.tail = self.tail.prev_node
            else:
                while(tmp.data != node_value and tmp != self.tail):
                    tmp = tmp.next_node
                if (tmp != self.tail):
                    tmp.prev_node.next_node = tmp.next_node
                    tmp.next_node.prev_node = tmp.prev_node
                else:
                    raise ValueError("Node Value does not exist")
    
    def printList(self):
        s = self.size()
        tmp = self.head
        for i in range(s):
            print tmp.data,
            tmp = tmp.next_node
            
    def size(self):
        cnt = 0
        if self.head == self.tail:
            return cnt
        tmp = self.head
        while(tmp != self.tail):
            cnt += 1
            tmp = tmp.next_node
        cnt += 1
        return cnt
        


# In[62]:


dlst = dlist()


# In[63]:


dlst.insertNODE(1)


# In[64]:


print dlst.size()


# In[65]:


dlst.printList()


# In[66]:


dlst.insertNODE(2)


# In[67]:


print dlst.size()


# In[68]:


dlst.insertNODE(3)


# In[69]:


print dlst.size()


# In[70]:


for i in range(4,11):
    dlst.insertNODE(i)


# In[71]:


dlst.printList()


# In[72]:


dlst.deleteNODE(3)


# In[73]:


print dlst.size()


# In[74]:


dlst.printList()


# In[75]:


dlst.deleteNODE(10)


# In[76]:


dlst.printList()


# In[77]:


dlst.deleteNODE(1)


# In[78]:


dlst.printList()


# In[79]:


dlst.deleteNODE(11)


# In[80]:


d1 = dlist()


# In[81]:


d1.size()


# In[82]:


d1.deleteNODE(9)


# In[ ]:




