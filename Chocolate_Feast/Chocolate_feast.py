def chocolateFeast(n, c, m):
    num_choc = n // c
    num_wrapper = num_choc
    while num_wrapper >= m:
        more_choc = num_wrapper // m
        num_wrapper = num_wrapper % m + more_choc
        num_choc += more_choc
    
    return num_choc
