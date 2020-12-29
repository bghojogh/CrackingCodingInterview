import numpy as np

def main():
    stack = Stack()
    stack.push(value=10)
    stack.push(value=2)
    stack.push(value=6)
    print(stack.get_min())
    print(stack.pop())
    print(stack.get_min())
    print(stack.pop())
    print(stack.get_min())
    print(stack.pop())

class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_beneath = []
        self.min_ = np.inf
        
    def push(self, value):
        if len(self.stack) == 0:
            self.min_ = value
        else:
            self.min_ = min(value, self.min_)
        self.min_beneath.append(self.min_)
        self.stack.append(value)
        
    def pop(self):
        return self.stack.pop()
    
    def get_min(self):
        return self.min_beneath.pop()

if __name__ == '__main__':
    main()