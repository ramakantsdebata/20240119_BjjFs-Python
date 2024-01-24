def fileBinWriteList():
    lst = [1.7, 2.4, 3.9]
    f = open("BinaryFile.bin", mode = 'wb')
    for x in lst:
        s = str(x) + "\n"
        bt = s.encode()
        f.write(bt)
    f.close()


def fileBinReadList():
    lst = []
    f = open("BinaryFile.bin", 'rb')
    for line in f:
        x = float(line)
        lst.append(x)
        print("List ->", lst)
    f.close()

## Use Struct Packing & Unpacking #############

import struct 

def fileBinWriteListStruct():
    lst = [1.7, 2.4, 3.9]
    print("Packing the list -->", lst)
    st = struct.pack('f'*len(lst), *lst)
    f = open("BinaryFilePacked.bin", mode = 'wb')
    f.write(st)
    f.close()

def fileBinReadListStruct():
    upLst = []
    f = open("BinaryFilePacked.bin", 'rb')
    data = f.read()
    upLst = struct.unpack('f'*3, data)
    f.close()
    print("Unpacked list ->", upLst)

if __name__ == "__main__":
    fileBinWriteList()
    fileBinReadList()
    print("\n", "-"*10)
    fileBinWriteListStruct()
    fileBinReadListStruct()