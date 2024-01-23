lst = []
lst.append(lambda x: x * x)
print(lst[0](5))

sq = lambda x: x * x
isEven = lambda x: x % 2 == 0
nextEven = lambda x: x+2 if x % 2 == 0 else x+1

print(sq(2))
print(isEven(2))
print(nextEven(2))
print(nextEven(73))


def sort(arr, comparator):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if comparator(arr[i], arr[j]):
                arr[i], arr[j] = arr[j], arr[i]


arr = []

def compare_date(a, b):
    return not(a.getDate() > b.getDate())

def compare_amt(a, b):
    pass

def compare_str(a, b):
    pass

sort(arr, lambda a, b: not(a.getDate() > b.getDate()))
sort(arr, compare_amt)
sort(arr, compare_str)

