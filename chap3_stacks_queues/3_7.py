import numpy as np

def main():
    queue = Queue()
    queue.enqueue(value="cat")
    queue.enqueue(value="cat")
    queue.enqueue(value="cat")
    queue.enqueue(value="dog")
    queue.enqueue(value="cat")
    print(queue.queue)
    print(queue.dequeueDog())
    print(queue.dequeueDog())
    print(queue.dequeueCat())
    print(queue.queue)

class Queue(object):
    def __init__(self):
        self.queue = []
        
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeueAny(self):
        return self.queue.pop(0)
    
    def dequeueDog(self):
        index = 0
        while index <= len(self.queue) - 1:
            if self.queue[index] == "dog":
                return self.queue.pop(index)
            index += 1
        return "no dog in queue"
    
    def dequeueCat(self):
        index = 0
        while index <= len(self.queue) - 1:
            if self.queue[index] == "cat":
                return self.queue.pop(index)
            index += 1
        return "no dog in queue" 

if __name__ == '__main__':
    main()