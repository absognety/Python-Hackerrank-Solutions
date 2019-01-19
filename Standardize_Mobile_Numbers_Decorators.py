def wrapper(f):
    def fun(l):
        len_numbers = [len(phone_num) for phone_num in l]
        for i in range(len(l)):
            if len_numbers[i]==10:
                l[i] = '+91' + ' ' + l[i][:5] + ' ' + l[i][5:]
            elif len_numbers[i]==11:
                l[i] = '+91' + ' ' + l[i][1:][:5] + ' ' + l[i][1:][5:]
            elif len_numbers[i]==12:
                l[i] = '+91' + ' ' + l[i][2:][:5] + ' ' + l[i][2:][5:]
            elif len_numbers[i]==13:
                l[i] = '+91' + ' ' + l[i][3:][:5] + ' ' + l[i][3:][5:]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
