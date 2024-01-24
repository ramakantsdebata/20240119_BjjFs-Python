class A:
    def __init__(self, x, y):
        self.p = x
        self.q = y

    def add(self):
        return self.p + self.q


class B:
    def __init__(self, x, y):
        self.p = x
        self.q = y

    def add(self):
        return self.p + self.q
    
    def sub(self):
        return self.p - self.q

def operate(obj: B):
    print(obj.add())
    print(obj.sub())

if __name__ == "__main__":
    a = A(10, 20)
    b = B(10, 20)

    operate(b)
    operate(a) # Works for add, not subtract

