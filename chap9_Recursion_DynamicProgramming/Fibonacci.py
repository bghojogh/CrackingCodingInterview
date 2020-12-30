import numpy as np

def main():
    print("=============================== Recursive Approach:")
    for n in range(10):
        print(Fibonacci_recursive(n))
    print("=============================== Iterative Approach:")
    print(Fibonacci_iterative(n=10))
    print("=============================== Dynamic Programming Approach:")
    for n in range(10):
        f_dp = Fibonacci_DynamicProgramming()
        print(f_dp.calculate(n))

def Fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)

def Fibonacci_iterative(n):
    array = []
    for i in range(n):
        if i == 0 or i == 1:
            array.append(i)
            continue
        array.append(array[i-1] + array[i-2])
    return array

class Fibonacci_DynamicProgramming(object):
    def __init__(self):
        self.array = [0, 1]
        
    def calculate(self, n):
        if n == 0 or n == 1:
            return n
        try:
            if self.array[n] is not None:
                return self.array[n]
        except:
            pass
        self.array.append(self.calculate(n-1) + self.calculate(n-2))
        # print(n)
        # print(len(self.array))
        return self.array[n]
            
if __name__ == '__main__':
    main()