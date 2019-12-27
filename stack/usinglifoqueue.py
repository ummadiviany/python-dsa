from queue import LifoQueue

stack=LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')
print(stack.full())
print("Elements of stack:")
print(stack)
print("Popping elements from stack:")
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.qsize())
print(stack.empty())
#print(stack.get())