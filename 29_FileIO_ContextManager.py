fileName = "stuff.txt"

def fileTextWrite():
    # f = open(fileName, "wt", encoding = 'utf-8')
    with open (fileName, "wt", encoding = 'utf-8') as f:
        f.writelines("{0}\n".format(x) for x in range(100))

def fileTextRead():
    with open (fileName, "rt", encoding = 'utf-8') as f:
        sqSeq = [int(line.strip()) ** 2 for line in f]
    print(sqSeq)

    # Using context mgr to manage any object lifetime    
    # with Cab() as c1:
    #     c1.book()
    #     c1.drive("dest1")
    #     c1.refill()
    # print("Done with our trip")
    
if __name__ == "__main__":
    fileTextWrite()
    fileTextRead()
    print("Done!")