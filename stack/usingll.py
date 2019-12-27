class StackNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.root=None
    
    def isEmpty(self):
        return True if self.root is None else False
    
    def push(self,data):
        new_node=StackNode(data)
        new_node.next=self.root
        self.root=new_node
        print("%d Pushed to stack"%(data))
    
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp=self.root
        self.root=self.root.next
        popped =temp.data
        return popped
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

if __name__ == "__main__":
    stack=Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("%d popped from stack"%(stack.pop()))
    print("%d Top element of stack"%(stack.peek()))
    print(stack)