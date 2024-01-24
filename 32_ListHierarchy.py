class SimpleList:
    def __init__(self, items):
        print("SimpleList")
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, idx):
        return self._items[idx]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"


class SortedList(SimpleList):
    def __init__(self, items=()):
        print("SortedList")
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def getSuper(self):
        return super()


class IntList(SimpleList):
    def __init__(self, items=()):
        print("IntList")
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(obj):
        if not isinstance(obj, int):
            raise TypeError("IntList only supports integer values")
        
    def add(self, item):
        self._validate(item)
        super().add(item)

    def getSuper(self):
        return super()
    

class SortedIntList(IntList, SortedList):
    def __init__(self, items=()):
        print("SortedIntList")
        super().__init__(items)

#################################################

if __name__ == "__main__":
    sl1 = SortedList([77, 12, 23, 87])
    sl1.add(5)
    print(sl1[1])
    print(sl1)

    try:
        il1 = IntList([77, 13, 23, 87])
        il1.add("Test")
    except TypeError as e:
        print(e)
    
    print("\n")
    print("SortedList Super ->", sl1.getSuper(), " ", type(sl1).__bases__)
    print("IntList Super ->", il1.getSuper(), " ", type(il1).__bases__)

    print("\n")
    sil1 = SortedIntList([77, 13, 23, 87])
    sil1.add(5)
    print(sil1)
    try:
        sil1.add(3.5)
    except TypeError as e:
        print(e)

    print(sil1)
    print("\n\t", sil1.getSuper(), "\n\t", type(sil1).__bases__)
 

    # MRO: Method Resolution Order
    print("\n")
    print(SortedIntList.__mro__)
    