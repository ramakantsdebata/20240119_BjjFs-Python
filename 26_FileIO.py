# CodePoints

# struct FILE* f
# ret = write() - no. of bytes
# read - no. of bytes to read

# ASCII - 1 char
# Widechars - 1/2 char

# open / close - Open Mode -- r, w, x, a, r+, w+, a+, rb, wb, ab, rb+,
# write / read
# -------- / readline
# writelines / readlines

# seek / tell

# Whence - Begin, End, Curr
# Offset -  + -

import sys
# print(sys.getdefaultencoding())

fileName = "stuff.txt"

def fileTextWrite():
    f = open(fileName, "wt", encoding = 'utf-8')
    charsWritten = f.write('What are the roots that clutch, ')
    print("Characters/Codepoints witten:", charsWritten)

    f.write('what branches grow\n')
    f.write('Out of this stony rubbish?')
    f.close()


def fileTextRead():
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

    f.close()
    
def fileTextRead2():
    print("\nRead with for loop")
    f = open(fileName, "rt", encoding = 'utf-8')
    for line in f:
        # print(line)
        sys.stdout.write(line)
    f.close()
    
if __name__ == "__main__":
    fileTextWrite()
    fileTextRead()
    fileTextRead2()