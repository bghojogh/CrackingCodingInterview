import numpy as np

def main():
    queue = MyQueue()
    queue.push(value=10)
    queue.push(value=2)
    queue.push(value=6)
    queue.push(value=3)
    queue.push(value=1)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    queue.push(value=7)
    queue.push(value=8)
    print(queue.pop())
    print(queue.pop())

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.active_stack = 1
        
    def push(self, value):
        if self.active_stack == 1:
            self.stack1.append(value)
        elif self.active_stack == 2:
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            self.stack1.append(value)
            self.active_stack = 1
        
    def pop(self):
        if self.active_stack == 1:
            for i in range(len(self.stack1)-1):
                self.stack2.append(self.stack1.pop())
            self.active_stack = 2
            return self.stack1.pop()
        elif self.active_stack == 2:
            return self.stack2.pop()

if __name__ == '__main__':
    main()