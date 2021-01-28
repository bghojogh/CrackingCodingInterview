def main():
    a = A(n=10)
    a.compute()
    b = B(n=10)
    b.compute()

#### output:
# 30
# 30
# 40
    
class A(object):
    def __init__(self, n):
        self.n = n
        
    def compute(self):
        print(self.n * 3)
        
class B(A):
    def __init__(self, n):
        self.n = n
        super().compute()
        
    def compute(self):
        print(self.n * 4)
        
if __name__ == '__main__':
    main()