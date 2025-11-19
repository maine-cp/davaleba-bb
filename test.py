from stack import Stack
from queue import Queue

print("=== STACK TEST (LIFO) ===")
s = Stack()


for i in range(1, 6):
    s.push(i)


print("Popped:", s.pop())
print("Popped:", s.pop())
print("Popped:", s.pop())


print("Peek:", s.peek())        
print("Size:", s.size())        


print("\n=== QUEUE TEST (FIFO) ===")
q = Queue()

for i in range(1, 6):
    q.enqueue(i)


print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())

print("Front:", q.front())      
print("Size:", q.size())        
