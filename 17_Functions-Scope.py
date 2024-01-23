str1 = "Global String"

def Outer():
    # global str1
    str1 = "Local String"

    print("Locals:", locals())
    print("Globals:", globals())
    globals()['str1'] = "Modified Global string"
    def Inner():
        # global str1
        # nonlocal str1
        str1 = "Inner String"
        print("Inner:", str1)

    print("Outer:", str1)
    return Inner

def main():
    # func = Outer()
    # func()
    Outer()()
    print("Global:", str1)

main()