import numpy as np

def main():
    stacks = Stacks(stack_size=20)
    stacks.push(value=2, stack_index=0)
    stacks.push(value=4, stack_index=0)
    stacks.push(value=6, stack_index=0)
    print(stacks.pop(stack_index=0))
    print(stacks.pop(stack_index=0))
    print(stacks.pop(stack_index=0))
    
    stacks.push(value=12, stack_index=1)
    stacks.push(value=14, stack_index=1)
    stacks.push(value=16, stack_index=1)
    print(stacks.pop(stack_index=1))
    print(stacks.pop(stack_index=1))
    print(stacks.pop(stack_index=1))
    
    stacks.push(value=120, stack_index=2)
    stacks.push(value=140, stack_index=2)
    stacks.push(value=160, stack_index=2)
    print(stacks.pop(stack_index=2))
    print(stacks.pop(stack_index=2))
    print(stacks.peek(stack_index=2))
    print(stacks.pop(stack_index=2))
    print(stacks.pop(stack_index=2))

class Stacks(object):
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack_pointers = [-1, -1, -1]
        self.array_ = np.zeros((stack_size*3,))
        
    def push(self, value, stack_index):
        self.stack_pointers[stack_index] += 1
        self.array_[(stack_index * self.stack_size) + self.stack_pointers[stack_index]] = value
        
    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise ValueError("Empty Stack")
        value = self.array_[(stack_index * self.stack_size) + self.stack_pointers[stack_index]]
        self.array_[(stack_index * self.stack_size) + self.stack_pointers[stack_index]] = 0
        self.stack_pointers[stack_index] -= 1
        return value
    
    def peek(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise ValueError("Empty Stack")
        value = self.array_[(stack_index * self.stack_size) + self.stack_pointers[stack_index]]
        return value

if __name__ == '__main__':
    main()