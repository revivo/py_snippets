__author__ = 'deezzy'

#
#    Write a simple application which extends the stack data structure interface by adding a method for retrieving
#    the minimum value in the stack.
#

import sys
import heapq


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class MinItemStack(Stack):

    def __init__(self):
        self.stack = Stack()
        self.min_item = sys.maxint
        self.min_heap = []

    def pop(self):
        item = self.stack.pop()
        self.min_heap.remove(item)
        heapq.heapify(self.min_heap)
        self.min_item = min(self.min_heap)

    def get_min(self):
        return self.min_item

    def push(self, item):
        if item < self.min_item:
            self.min_item = item
        heapq.heappush(self.min_heap, item)
        self.stack.push(item)



min_stack = MinItemStack()


min_stack.push(5)
print min_stack.get_min()
print '----'
print min_stack.stack.items
print '----'
min_stack.push(24)
print min_stack.get_min()
print '----'
print min_stack.stack.items
min_stack.push(2)
print '----'
print min_stack.get_min()
print '----'
print min_stack.stack.items
min_stack.push(5)
print '----'
print min_stack.get_min()
print '----'
print min_stack.stack.items
min_stack.push(1)
print '----'
print min_stack.get_min()
print '----'
print min_stack.stack.items
print '---- start pop ----'


min_stack.pop()
print min_stack.get_min()
print '----'
print min_stack.stack.items

print '----'
min_stack.pop()
print min_stack.get_min()
print '----'
print min_stack.stack.items
print '----'

min_stack.pop()
print min_stack.get_min()
print min_stack.stack.items

min_stack.pop()
print min_stack.get_min()
print min_stack.stack.items


min_stack.pop()
print min_stack.get_min()
print min_stack.stack.items
