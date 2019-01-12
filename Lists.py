if __name__ == '__main__':
    N = int(input())
    l = []
for i in range(N):
    name = input()
    spl = str.split(name)
    if len(spl) == 3:
        com = str(spl[0])
        ind = int(spl[1])
        obj = int(spl[2])
    elif len(spl) == 2:
        com = str(spl[0])
        obj = int(spl[1])
    elif len(spl) == 1:
        com = str(spl[0])
    if com == "insert":
        l.insert(ind,obj)
    elif com == "print":
        print (l)
    elif com == "remove":
        l.remove(obj)
    elif com == "append":
        l.append(obj)
    elif com == "sort":
        l.sort()
    elif com == "pop":
        l.pop()
    else:
        l.reverse()
