### Implementation of simple stack

class stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items += [item]

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = stack()

for i in range(10):
    s.push(i)

for i in range(10):
    print s.pop()




