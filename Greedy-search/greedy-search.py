smalls = [1]
smallf = [0, 4]

start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m < n and s[m] < f[k]:
        m = m + 1
    if m < n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


def greedy_activity_selector(s, f):
    assert(len(s) == len(f))
    n = len(s)
    a = []
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            a.append(m)
            k = m
    return a