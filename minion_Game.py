import itertools
import string
def minionGame(STR):
    stuart_score = 0
    kevin_score = 0
    combs_list = []
    len_S = len(STR)
    for v in range(1,len_S+1):
        combins = list(itertools.combinations(STR,v))
        combins = [''.join(r) for r in combins]
        combs_list.extend(combins)
    for c in combs_list:
        if c[0].isupper():
            if c[0] in set(string.ascii_uppercase)-set('AEIOU'):
                stuart_score+=1
            else:
                kevin_score+=1
    if stuart_score>kevin_score:
        return ('Stuart', stuart_score)
    elif stuart_score<kevin_score:
        return ('Kevin', kevin_score)
    elif stuart_score==kevin_score:
        return 'Draw'
    
if __name__ == '__main__':
    s = input()
    print (minionGame(s))
    