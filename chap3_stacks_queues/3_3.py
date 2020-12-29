import numpy as np

def main():
    stack = SetOfStacks(threshold_=2)
    stack.push(value=10)
    stack.push(value=2)
    stack.push(value=6)
    stack.push(value=3)
    stack.push(value=1)
    print(stack.stacks)
    print(stack.pop())
    print(stack.pop())
    print(stack.popAt(1))
    print(stack.popAt(2))

class SetOfStacks(object):
    def __init__(self, threshold_):
        self.stacks = [[]]
        self.threshold_ = threshold_
        self.latest_stack_index = 0
        
    def push(self, value):
        if len(self.stacks[-1]) >= self.threshold_:
            self.stacks.append([value])
            self.latest_stack_index += 1
        else:
            self.stacks[self.latest_stack_index].append(value)
        
    def pop(self):
        value = self.stacks[self.latest_stack_index].pop()
        if len(self.stacks[self.latest_stack_index]) == 0:
            self.latest_stack_index -= 1
        return value
    
    def popAt(self, stack_index):
        if stack_index > self.latest_stack_index:
            raise ValueError("invalid index")
        return self.stacks[stack_index].pop()

if __name__ == '__main__':
    main()