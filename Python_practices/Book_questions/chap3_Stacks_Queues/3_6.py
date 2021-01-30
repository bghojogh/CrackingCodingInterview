import numpy as np

def main():
    stack_ = Stack()
    stack_.push1(value=10)
    stack_.push1(value=2)
    stack_.push1(value=6)
    stack_.push1(value=3)
    stack_.push1(value=1)
    print(stack_.sort_assending())

class Stack(object):
    def __init__(self):
        self.stack = []
        self.buffer = []
        
    def push1(self, value):
        self.stack.append(value)
        
    def pop1(self):
        return self.stack.pop()
    
    def peek1(self):
        return self.stack[-1]
    
    def is_empty1(self):
        return len(self.stack) == 0
    
    def push2(self, value):
        self.buffer.append(value)
        
    def pop2(self):
        return self.buffer.pop()
    
    def peek2(self):
        return self.buffer[-1]
    
    def is_empty2(self):
        return len(self.buffer) == 0
    
    def sort_assending(self):
        while not self.is_empty1():
            value = self.stack.pop()
            while True:
                if len(self.buffer) == 0:
                    self.buffer.append(value)
                    break
                if self.peek2() > value:
                    self.stack.append(self.buffer.pop())
                else:
                    self.buffer.append(value)
                    break
            # print(self.buffer)
            # print(self.stack)
        self.stack = self.buffer
        self.buffer = []
        return self.stack
                

if __name__ == '__main__':
    main()