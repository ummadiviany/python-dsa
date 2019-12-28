class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,item):
        if((self.rear+1)%self.size==self.front):
            print("Queue is Full")
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=item
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=item
    def dequeue(self):
        if self.front==-1:
            print("Queue is Empty")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("Queue is EMpty")
        elif(self.rear>=self.front):
            print("Elements in the circular queue are :",end="")
            for i in range (self.front,self.rear+1):
                print(self.queue[i],end="")
            print()
        else:
            print("Elements in the circular queue are :",end="")
            for i in range (self.front,self.size):
                print(self.queue[i],end="")
            for i in range (0,self.rear+1):
                print(self.queue[i],end="")
            print()
        if((self.rear+1)%self.size==self.front):
            print("Queue is Full")


if __name__=="__main__":
    cq=CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.display()
    print ("Deleted value = ", cq.dequeue()) 
    print ("Deleted value = ", cq.dequeue())
    cq.display()
    cq.enqueue(5)
    cq.enqueue(6)
    cq.enqueue(7)
    cq.display() 
