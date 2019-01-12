if __name__ == '__main__':
    s = input()
    sl = list(s)
    print (any(c.isalnum() for c in sl))
    print (any(c.isalpha() for c in sl))
    print (any(c.isdigit() for c in sl))
    print (any(c.islower() for c in sl))
    print (any(c.isupper() for c in sl))