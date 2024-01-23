def Foo():
    print("Foo")
    raise IndexError("Foo Exception")

def Bar():
    print("Bar")
    try:
        # Open connection
        # Create connection Object
        Foo()
        # (1) Close connection
    except (StopIteration, IndexError) as e:
        # print("StopIteration Exception caught")
        print("Cleanup for ", e)
        print("Notify caller")
        # raise
        # (2) Close connection
    finally:
       # Close connection here
        print("Close connection here")
    
    # (3) Close connection
    print("Returning from Bar")

def Main():
    print("Main")
    try:
        Bar()
    except ValueError:
        print("ValueError Exception caught")
    except Exception:
        print("Unhandled Exception caught")
    print("Exiting Main")

if __name__ == "__main__":
    Main()