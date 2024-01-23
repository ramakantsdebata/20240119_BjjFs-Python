l1 = [1, 2]

def Foo(l1):
    l1.append(3)
    l1 = ['a', 'b']
    print("Foo:", l1)

def Bar():
    print(l1)

def main():
    Foo(l1)
    print("Main:", l1)

main()