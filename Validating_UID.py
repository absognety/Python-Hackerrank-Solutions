# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
T = int(input())
for tcase in range(T):
    UID = input()
    UID = ''.join(sorted(UID))
    try:
        assert re.search(r'[A-Z]{2}', UID)
        assert re.search(r'\d\d\d', UID)
        assert not re.search(r'[^a-zA-Z0-9]', UID)
        assert not re.search(r'(.)\1',UID)
        assert len(UID) == 10
    except:
        print('Invalid')
    else:
        print('Valid')