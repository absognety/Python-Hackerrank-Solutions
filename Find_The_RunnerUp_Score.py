if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ar = list(arr)
    ar = list(set(ar))
    m = max(ar)
    ar.remove(m)
    l = []
    for i in range(len(ar)):
        l.append(m-ar[i])
    least_dif = min(l)
    for i in range(len(l)):
        if(l[i] == least_dif):
            print (ar[i])