# def my_generator():
#     print("Inside my_generator")
#     print("Publishing 'a'")
#     yield 'a'
#     print("Publishing 'b'")
#     yield 'b'
#     print("Publishing 'c'")
#     yield 'c'

# def main():
#     gen = my_generator()
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     # print(next(gen))

# main()

## Using generator to generate fibonacci series
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

def main():
    x = fib(5)
    print(x)
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))

main()