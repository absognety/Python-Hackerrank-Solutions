from itertools import groupby

S = input()
compress_str = [list(v) for k,v in groupby(S)]
ans = []
for C in compress_str:
    ans.append(str((len(C),int(C[0]))))
print (' '.join(ans))