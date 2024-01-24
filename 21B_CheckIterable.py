def isIterable(obj):
    try:
        iter(obj)
        return True
    except Exception:
        return False
    
if __name__ == "__main__":
    a = 10
    print(isIterable(a))
    b = "Hello"
    print(isIterable(b))
    c = [10, 2]
    print(isIterable(c))
    d = (10, 2)
    print(isIterable(d))
    e = {10, 2}
    print(isIterable(e))
    