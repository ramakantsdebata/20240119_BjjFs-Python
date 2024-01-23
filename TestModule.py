
__all__ = ["Testing", "sort"]

def swap(a, b):
    print("Swapping the values...")

def sort(arr):
    print("sorting...")
    # swapping
    a, b = 1, 2
    swap(a, b)

def Testing():
    print("Testing")

def main():
    print("Main called")
    Testing()

print("__name__:", __name__)

if __name__ == "__main__":
    main()  