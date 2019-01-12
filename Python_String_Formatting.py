def print_formatted(number):
    w = len(bin(number)[2:])
    for n in range(1,number+1):
        print (str(n).rjust(w,' '),str(oct(n)[2:]).rjust(w,' '),
               str(hex(n)[2:].upper()).rjust(w,' '),str(bin(n)[2:]).rjust(w,' '),sep=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
