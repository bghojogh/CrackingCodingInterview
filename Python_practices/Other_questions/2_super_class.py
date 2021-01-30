def main():
    a = A(n=10)
    a.compute()
    b = B(n=10)
    b.compute()

#### output:
# 100
# 400
    
class A(object):
    def __init__(self, n):
        self.n = n * 10
        
    def compute(self):
        print(self.n)
        
class B(A):
    def __init__(self, n):
        super().__init__(n)
        
    def compute(self):
        print(self.n * 4)
        
if __name__ == '__main__':
    main()