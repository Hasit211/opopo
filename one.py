def swapFileData():
    with open(hasit2.txt,'r') as a:
        data_a = a.read()
    with open(hasit.txt,'r') as b:
        data_b = b.read()
    with open(hasit2.txt,'w') as a:
        a.write(data_b)
    with open(hasit.txt,'w') as b:
        b.write(data_a)
swapFileData() 