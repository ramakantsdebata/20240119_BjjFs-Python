fileName = "stuff.txt"

def fileTextWrite():
    try:
        f = open(fileName, "wt", encoding = 'utf-8')
        charsWritten = f.write('What are the roots that clutch, ')
        print("Characters/Codepoints witten:", charsWritten)

        f.write('what branches grow\n')
        f.write('Out of this stony rubbish?')
    finally:
        f.close()


def fileTextRead():
    try:
        f = open(fileName, "rt", encoding = 'utf-8')
        s1 = f.read(32)
        print(s1)

        s1 = f.read()
        print(s1)

        s1 = f.read()
        if s1 == str(""):
            print("\n\tFile has been completely read through.")
        else:
            print(s1)

        # Navigation
        pos = f.seek(0)
        print(pos)
        s1 = f.readlines()

        print("\nRead with readlines function \n", s1)
    finally:
        f.close()
        
if __name__ == "__main__":
    fileTextWrite()
    fileTextRead()
    