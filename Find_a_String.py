def count_substring(string, sub_st):
    ans=[1 for i in range(len(string)-len(sub_st)+1) if string[i:i+len(sub_st)] == sub_st]
    ans = sum(ans)
    return ans

