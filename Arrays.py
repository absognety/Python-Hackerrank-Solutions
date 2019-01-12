def arrays(arr):
    import numpy as np
    arr.reverse()
    fl = list(map(float,arr))
    res = np.array(fl)
    return(res)