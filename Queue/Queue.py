class Queue:
    def __init__(self,capacity):
        self.front=self.size=0
        self.rear=capacity-1
        self.Q=[None]*capacity
        self.capacity=capacity
    def isFull(self):
        return self.size==self.capacity
    def isEmpty(self):
        return self.size==0
    def Enqueue(self,item):
        if self.isFull():
            print("Queue is FUll")
            return
        self.rear=(self.rear+1)%(self.capacity)
        self.Q[self.rear]=item
        self.size=self.size+1
        print("%s is added to Queue"%str(item))
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print("%s is removed from Queue"%str(self.Q[self.front]))
        self.front=(self.front+1)%(self.capacity)
        self.size=self.size-1
        
    def que_front(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print("Front item is %s"%str(self.Q[self.front]))
    def que_rear(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print("Rear item is %s"%str(self.Q[self.rear]))

if __name__=="__main__":
    queue=Queue(20)
    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    queue.Enqueue(5)
    queue.Dequeue()
    queue.que_front()
    queue.que_rear()