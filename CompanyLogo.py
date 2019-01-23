def companyLogo(s):
    literal_cnts = {}
    dist_letters = set(s)
    for char in dist_letters:
        literal_cnts[char] = s.count(char)
    sorted_kv = sorted(literal_cnts.items(),key=lambda x: (x[1],-ord(x[0])),reverse=True)
    top_3 = sorted_kv[:3]
    if top_3[0][1] == top_3[1][1] and top_3[0][1] > top_3[2][1]:
        top_3[:2] = sorted(top_3[:2])
    elif top_3[1][1] == top_3[2][1]:
        top_3[1:] = sorted(top_3[1:])
    elif top_3[0][1] == top_3[1][1] == top_3[2][1]:
        top_3 = sorted(top_3)
    for k,v in top_3:
        print (k,v)
        
if __name__ == '__main__':
    
    S = input()
    companyLogo(S)