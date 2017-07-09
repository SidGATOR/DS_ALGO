class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items [item]

    def addRear(self,item):
        return self.items.insert(0,item)

    def removeFront(self):
        if self.isEmpty():
            return "Deque is Empty"
        else:
            return self.items.pop()

    def removeRear(self):
        if self.isEmpty():
            return "Deque is Empty"
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)


