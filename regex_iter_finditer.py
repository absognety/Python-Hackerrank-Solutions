# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

vowels = r"[AEIOUaeiou]"
consonants = r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]"

s = input()

m = re.findall(
    rf"(?<={consonants}){vowels}" + "{2,}" + rf"(?={consonants})", s)
print("\n".join(m) if m else -1)