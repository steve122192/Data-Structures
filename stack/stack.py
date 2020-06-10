"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         l = self.storage
#         if len(l) == 0:
#             pass
#         else:  
#             popped = l[-1]
#             self.storage = l[:-1]
#             return popped


        
class Stack:
    def __init__(self, l=None):
        self.size = 0
        #self.storage = LinkedList()
        if l is None:
            l = LinkedList()
        self.l = l


    def __len__(self):
        count = 0
        head = self.storage.head
        tail = self.storage.tail
        done = False
        while done is False:
            if count == 0 and head is None:
                done = True
            elif count == 0 and head.get_next is None:
                count += 1
                done = True
            elif head is not tail:
                head = head.get_next()
                count += 1
            else:
                count += 1
                done = True
        return count

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()
